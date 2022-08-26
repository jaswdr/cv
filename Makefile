# Makefile for generating CV in multiple formats
# Author: Jonathan Schweder

# Variables
SOURCE = Jonathan_Schweder_CV.md
DOCX = Jonathan_Schweder_CV.docx
PDF = Jonathan_Schweder_CV.pdf
PANDOC = pandoc
PDFLATEX = pdflatex

# PDF configuration
PDF_ENGINE = --pdf-engine=$(PDFLATEX)
PDF_OPTIONS = -V geometry:margin=0.75in -V fontsize=10pt

# Default target
.DEFAULT_GOAL := all

# Phony targets (not actual files)
.PHONY: all clean docx pdf help watch

# Build all formats
all: docx pdf
	@echo "✓ All formats generated successfully!"
	@ls -lh $(DOCX) $(PDF)

# Generate DOCX
docx: $(DOCX)

$(DOCX): $(SOURCE)
	@echo "Generating DOCX..."
	@$(PANDOC) $(SOURCE) -o $(DOCX)
	@echo "✓ DOCX generated: $(DOCX)"

# Generate PDF
pdf: $(PDF)

$(PDF): $(SOURCE)
	@echo "Generating PDF..."
	@$(PANDOC) $(SOURCE) -o $(PDF) $(PDF_ENGINE) $(PDF_OPTIONS)
	@echo "✓ PDF generated: $(PDF)"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f $(DOCX) $(PDF)
	@rm -f *.aux *.log *.out *.toc
	@echo "✓ Clean complete!"

# Watch for changes and rebuild (requires inotify-tools)
watch:
	@echo "Watching $(SOURCE) for changes..."
	@echo "Press Ctrl+C to stop"
	@while true; do \
		inotifywait -e modify $(SOURCE) 2>/dev/null && \
		make all; \
	done

# Display help
help:
	@echo "CV Makefile - Available targets:"
	@echo ""
	@echo "  make          - Build all formats (DOCX and PDF)"
	@echo "  make all      - Build all formats (DOCX and PDF)"
	@echo "  make docx     - Generate DOCX only"
	@echo "  make pdf      - Generate PDF only"
	@echo "  make clean    - Remove all generated files"
	@echo "  make watch    - Watch for changes and auto-rebuild"
	@echo "  make help     - Display this help message"
	@echo ""
	@echo "Source file: $(SOURCE)"
	@echo "Output files: $(DOCX), $(PDF)"

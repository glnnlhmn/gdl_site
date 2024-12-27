# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

### [Unreleased]
#### Added

### [0.2.0] - 2024-12-27
#### Added
- **Project Structure Overhaul**
  - Reorganized project structure to improve maintainability.
  - Moved static and template files into the app directory.
- **Template Enhancements**
  - Created a base.html template for consistent layout across pages.
  - Added header.html and footer.html partials for modularity.
  - Introduced a menu.html partial for the navigation menu.
- **CSS and JS Integration**
  - Linked Bootstrap CSS and JS for responsive design.
  - Added custom styles in styles.css.
  - Included custom scripts in scripts.js.
- **Blueprint Setup**
  - Registered blueprints for modular route management.
- **Jinja2 Templating**
  - Implemented Jinja2 inheritance for efficient template management.
  - Used {% block %} and {% include %} for dynamic content rendering.
- **Error Fixes**
  - Resolved issues with static file paths.
  - Fixed url_for usage to correctly link static resources.
- **Documentation Updates**
  - Updated README with new project structure and setup instructions.
  - Added detailed comments in templates for clarity.

### [0.1.1] - 2024-12-25
#### Added
- Added section for work history gap

### [0.1.0] - 2024-10-25
#### Added
- Initial public release of the professional portfolio.
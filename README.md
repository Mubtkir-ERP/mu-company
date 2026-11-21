<!-- MUBTKIR-UNIFIED-README-START -->
## تخصيصات وإعدادات الشركة | Mu Company

تطبيق لإدارة التخصيصات والبيانات الأساسية للشركات والمنشآت داخل ERPNext.
* **الفئة المستهدفة:** الشركات والمجموعات التجارية العاملة على ERPNext.

Company-level customizations and core business configurations for ERPNext.
* **Target Audience:** Enterprises and multi-branch companies running ERPNext.

### تواصل معنا | Contact & Sales — [مبتكر للأنظمة السحابية | Mubtkir ERP](https://mubtkir.com)

* 🌐 **الموقع الرسمي | Website:** [Mubtkir ERP — حلول ERPNext السحابية](https://mubtkir.com)
* 📧 **البريد الإلكتروني | Email:** [sales@mubtkir.com](mailto:sales@mubtkir.com)
* 📱 **الجوال | Mobile:** [+966547706865](tel:+966547706865)
* 💬 **واتساب | WhatsApp:** [+966126810486](https://wa.me/966126810486)

<!-- MUBTKIR-UNIFIED-README-END -->

### Mu Company

Mu Company

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app mu_company
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/mu_company
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit

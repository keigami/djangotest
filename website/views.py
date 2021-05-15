from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "hogehoge"
        return ctxt


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = 133422222
        ctxt["skills"] = [
            "Python",
            "PHP",
            "C++",
            "HTML",
        ]
        return ctxt

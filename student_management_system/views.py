from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student,LibraryRecord,FeesRecord
from .forms import StudentForm,LibraryForm,FeesForm

class RoleRequiredMixin(UserPassesTestMixin):
    role_required = None
    def test_func(self):
        return self.request.user.role == self.role_required

# Admin Views
class AdminDashboardView(RoleRequiredMixin, ListView):
    model = Student
    template_name = 'dashboard.html'
    role_required = 'admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_student'] = Student.objects.count()
        context['total_library'] = LibraryRecord.objects.count()
        context['total_fees'] = FeesRecord.objects.count()
        return context
    
    
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        print("Form is valid!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid!", form.errors)
        return super().form_invalid(form)

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student-list')

class LibaryCreateView(CreateView):
    model = LibraryRecord
    form_class = LibraryForm
    template_name = 'library_form.html'
    success_url = reverse_lazy('library-list')

    def form_valid(self, form):
        print("Form is valid!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid!", form.errors)
        return super().form_invalid(form)
    
class LibraryListView(ListView):
    model = LibraryRecord
    template_name = 'library_list.html'

class LibaryUpdateView(UpdateView):
    model = LibraryRecord
    form_class = LibraryForm
    template_name = 'library_form.html'
    success_url = reverse_lazy('library-list')

class LibraryDeleteView(DeleteView):
    model = LibraryRecord
    template_name = 'library_confirm_delete.html'
    success_url = reverse_lazy('library-list')

class FeesListView(ListView):
    model = FeesRecord
    template_name = 'fees_list.html'

class FeesCreateView(CreateView):
    model = FeesRecord
    form_class = FeesForm
    template_name = 'fees_form.html'
    success_url = reverse_lazy('fees-list')

    def form_valid(self, form):
        print("Form is valid!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid!", form.errors)
        return super().form_invalid(form)

class FeesUpdateView(UpdateView):
    model = FeesRecord
    form_class = FeesForm
    template_name = 'fees_form.html'
    success_url = reverse_lazy('fees-list')

class FeesDeleteView(DeleteView):
    model = FeesRecord
    template_name = 'fees_confirm_delete.html'
    success_url = reverse_lazy('fees-list')


# class StudentListView(RoleRequiredMixin, ListView):
#     model = Student
#     template_name = 'school/student_list.html'
#     role_required = 'admin'

# class StudentCreateView(RoleRequiredMixin, CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'school/student_form.html'
#     success_url = reverse_lazy('student-list')
#     role_required = 'admin'

# class StudentUpdateView(RoleRequiredMixin, UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'school/student_form.html'
#     success_url = reverse_lazy('student-list')
#     role_required = 'admin'

# class StudentDeleteView(RoleRequiredMixin, DeleteView):
#     model = Student
#     template_name = 'school/student_confirm_delete.html'
#     success_url = reverse_lazy('student-list')
#     role_required = 'admin'

# # Librarian Views
# class LibrarianStudentDetailView(RoleRequiredMixin, DetailView):
#     model = Student
#     template_name = 'school/student_detail.html'
#     role_required = 'librarian'

# # Office Staff Views
# class StaffStudentListView(RoleRequiredMixin, ListView):
#     model = Student
#     template_name = 'school/student_list.html'
#     role_required = 'staff'

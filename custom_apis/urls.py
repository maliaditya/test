from django.urls import path
from .worker_details_views  import display_by_category, display_all, get_specific_worker_details
from .job_views import display_job,display_recruiter_job
from .requests_views import recruiters_requests, wokers_requests
from .status_update_views import recruiters_response, workers_response
from .recruiter_workers_response_views import display_workers_responses,display_recruiters_responses
from .verification_views import SendOtp
from .forgot_password_views import  enter_otp,passreset


urlpatterns =[
    #Worker_Details
    path('category/<str:category>/', display_by_category ),
    path('allcategories/', display_all ),
    path('specific/workerdetails/<int:user_id>', get_specific_worker_details ),

    #Job_Details
    path('specificjobs/<int:user>', display_job ),
    path('recruiterinfo/<int:recruiterid>',display_recruiter_job),

    #recruiters_requests
    path('recuriters/requests/<int:recruiter_id>',recruiters_requests),
    path('workers/requests/<int:worker_id>',wokers_requests),

    #Status_update
    path('recreq/<int:st>/<int:job_id>',recruiters_response),
    path('worreq/<int:st>/<int:job_id>',workers_response),

    #view_responses
    path('workers/responses/<int:worker_id>',display_workers_responses),
    path('recruiters/responses/<int:recruiter_id>',display_recruiters_responses),

    #verification
    path("user/<phone>/", SendOtp.as_view(), name="OTP Gen"),
    path("otp/", enter_otp),



    #Template
    path("reset_password/<int:phone>", passreset),


]
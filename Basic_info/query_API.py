import os
import time
import uuid
import hashlib
import random
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import connection
from django.shortcuts import render, redirect
from apple import settings
from Basic_info.models import *
from Order.models import *
import json
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required

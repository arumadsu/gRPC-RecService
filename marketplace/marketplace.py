import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
import pytest
import requests
import requests_mock

from .. import profiles, sizes, service, images

@pytest.fixture(scope="module")
def get_adapter():
  pass

@pytest.fixture(scope="module")
def get_profiles():
  return profiles.SingleuserProfiles(namespace="jsp-testing", verify_ssl=False)

@pytest.fixture(scope="module")
def loaded_profiles(get_profiles):
    _profiles = get_profiles
    _profiles.load_profiles()
    return _profiles

@pytest.fixture(scope="module")
def get_image_object(get_profiles):
  get_profiles.load_profiles()
  return images.Images(get_profiles.openshift, get_profiles.namespace)

@pytest.fixture(scope="module")
def get_service_object(get_profiles):
  get_profiles.load_profiles()
  return service.Service(get_profiles.openshift, get_profiles.namespace)

@pytest.fixture(scope="module")
def get_size_object(get_profiles):
  get_profiles.load_profiles()
  return sizes.Sizes(get_profiles.sizes)
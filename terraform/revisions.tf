locals {
  mysql_revisions = {
    amd64 = 240,
    arm64 = 274 # candidate
  }
  s3_integrator_revisions = {
    amd64 = 31,
    arm64 = 32
  }
  data_integrator_revisions = {
    amd64 = 41,
    arm64 = 40
  }
  mysql_router_revisions = {
    amd64 = 224,
    arm64 = 225
  }
  tls_revisions = {
    amd64 = 155,
    arm64 = 201
  }
}

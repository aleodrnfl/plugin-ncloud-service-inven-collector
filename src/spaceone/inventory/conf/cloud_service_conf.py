MAX_WORKER = 20
SUPPORTED_RESOURCE_TYPE = ['inventory.CloudService', 'inventory.CloudServiceType', 'inventory.Region',
                           'inventory.ErrorResource']
SUPPORTED_FEATURES = ['garbage_collection']
SUPPORTED_SCHEDULES = ['hours']
FILTER_FORMAT = []
CLOUD_SERVICE_GROUP_MAP = {
    'Compute': [
        'ServerManager'
    ]
}

ASSET_URL = 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/naver_cloud'

REGION_INFO = {
    "asia-east1": {"name": "Taiwan (Changhua County)",
                   "tags": {"latitude": "24.051196", "longitude": "120.516430", "continent": "asia_pacific"}},
    "asia-east2": {"name": "Hong Kong",
                   "tags": {"latitude": "22.283289", "longitude": "114.155851", "continent": "asia_pacific"}},
    "asia-northeast1": {"name": "Japan (Tokyo)",
                        "tags": {"latitude": "35.628391", "longitude": "139.417634", "continent": "asia_pacific"}},
    "asia-northeast2": {"name": "Japan (Osaka)",
                        "tags": {"latitude": "34.705403", "longitude": "135.490119", "continent": "asia_pacific"}},
    "asia-northeast3": {"name": "South Korea (Seoul)",
                        "tags": {"latitude": "37.499968", "longitude": "127.036376", "continent": "asia_pacific"}},
    "asia-south1": {"name": "India (Mumbai)",
                    "tags": {"latitude": "19.164951", "longitude": "72.851765", "continent": "asia_pacific"}},
    "asia-south2": {"name": "India (Delhi)",
                    "tags": {"latitude": "28.644800", "longitude": "77.216721", "continent": "asia_pacific"}},
    "asia-southeast1": {"name": "Singapore (Jurong West)",
                        "tags": {"latitude": "1.351376", "longitude": "103.709574", "continent": "asia_pacific"}},
    "asia-southeast2": {"name": "Indonesia (Jakarta)",
                        "tags": {"latitude": "-6.227851", "longitude": "106.808169", "continent": "asia_pacific"}},
    "australia-southeast1": {"name": "Australia (Sydney)", "tags": {"latitude": "-33.733694", "longitude": "150.969840",
                                                                    "continent": "asia_pacific"}},
    "australia-southeast2": {"name": "Australia (Melbourne)",
                             "tags": {"latitude": "-37.840935", "longitude": "144.946457",
                                      "continent": "asia_pacific"}},
    "europe-north1": {"name": "Finland (Hamina)",
                      "tags": {"latitude": "60.539504", "longitude": "27.113819", "continent": "europe"}},
    "europe-west1": {"name": "Belgium (St.Ghislain)",
                     "tags": {"latitude": "50.471248", "longitude": "3.825493", "continent": "europe"}},
    "europe-west2": {"name": "England, UK (London)",
                     "tags": {"latitude": "51.515998", "longitude": "-0.126918", "continent": "europe"}},
    "europe-west3": {"name": "Germany (Frankfurt)",
                     "tags": {"latitude": "50.115963", "longitude": "8.669625", "continent": "europe"}},
    "europe-west4": {"name": "Netherlands (Eemshaven)",
                     "tags": {"latitude": "53.427625", "longitude": "6.865703", "continent": "europe"}},
    "europe-west6": {"name": "Switzerland (Zürich)",
                     "tags": {"latitude": "47.365663", "longitude": "8.524881", "continent": "europe"}},
    "northamerica-northeast1": {"name": "Canada, Québec (Montréal)",
                                "tags": {"latitude": "45.501926", "longitude": "-73.570086",
                                         "continent": "north_america"}},
    "northamerica-northeast2": {"name": "Canada, Ontario (Toronto)",
                                "tags": {"latitude": "50.000000", "longitude": "-85.000000",
                                         "continent": "north_america"}},
    "southamerica-east1": {"name": "Brazil, São Paulo (Osasco)",
                           "tags": {"latitude": "43.8345", "longitude": "2.1972", "continent": "south_america"}},
    "southamerica-west1": {"name": "Chile (Santiago)",
                           "tags": {"latitude": "-33.447487", "longitude": "-70.673676", "continent": "south_america"}},
    "us-central1": {"name": "US, Iowa (Council Bluffs)",
                    "tags": {"latitude": "41.221419", "longitude": "-95.862676", "continent": "north_america"}},
    "us-east1": {"name": "US, South Carolina (Moncks Corner)",
                 "tags": {"latitude": "33.203394", "longitude": "-79.986329", "continent": "north_america"}},
    "us-east4": {"name": "US, Northern Virginia (Ashburn)",
                 "tags": {"latitude": "39.021075", "longitude": "-77.463569", "continent": "north_america"}},
    "us-west1": {"name": "US, Oregon (The Dalles)",
                 "tags": {"latitude": "45.631800", "longitude": "-121.200921", "continent": "north_america"}},
    "us-west2": {"name": "US, California (Los Angeles)",
                 "tags": {"latitude": "34.049329", "longitude": "-118.255265", "continent": "north_america"}},
    "us-west3": {"name": "US, Utah (Salt Lake City)",
                 "tags": {"latitude": "40.730109", "longitude": "-111.951386", "continent": "north_america"}},
    "us-west4": {"name": "US, Nevada (Las Vegas)",
                 "tags": {"latitude": "36.092498", "longitude": "-115.086073", "continent": "north_america"}},
    "global": {"name": "Global"}
}

OAUTH_SCOPES = {
    'https://www.naverapis.com/auth/cloud-platform': 'See, edit, configure, and delete your Naver Cloud data and see the email address for your Naver Account.',
    'https://www.naverapis.com/auth/cloud-platform.read-only': 'View your data across Naver Cloud services and see the email address of your Naver Account',
    'https://www.naverapis.com/auth/adexchange.buyer': 'Manage your Ad Exchange buyer account configuration',
    'https://www.naverapis.com/auth/admob.readonly': 'See your AdMob data',
    'https://www.naverapis.com/auth/admob.report': 'See your AdMob data',
    'https://www.naverapis.com/auth/adsensehost': 'View and manage your AdSense host data and associated accounts',
    'https://www.naverapis.com/auth/admin.reports.audit.readonly': 'View audit reports for your G Suite domain',
    'https://www.naverapis.com/auth/admin.reports.usage.readonly': 'View usage reports for your G Suite domain',
    'https://www.naverapis.com/auth/admin.datatransfer': 'View and manage data transfers between users in your organization',
    'https://www.naverapis.com/auth/admin.datatransfer.readonly': 'View data transfers between users in your organization',
    'https://www.naverapis.com/auth/admin.chrome.printers': 'See, add, edit, and permanently delete the printers that your organization can use with Chrome',
    'https://www.naverapis.com/auth/admin.chrome.printers.readonly': 'See the printers that your organization can use with Chrome',
    'https://www.naverapis.com/auth/admin.directory.customer': 'View and manage customer related information',
    'https://www.naverapis.com/auth/admin.directory.customer.readonly': 'View customer related information',
    'https://www.naverapis.com/auth/admin.directory.device.chromeos': "View and manage your ChromeOS devices' metadata",
    'https://www.naverapis.com/auth/admin.directory.device.chromeos.readonly': "View your ChromeOS devices' metadata",
    'https://www.naverapis.com/auth/admin.directory.device.mobile': "View and manage your mobile devices' metadata",
    'https://www.naverapis.com/auth/admin.directory.device.mobile.action': 'Manage your mobile devices by performing administrative tasks',
    'https://www.naverapis.com/auth/admin.directory.device.mobile.readonly': "View your mobile devices' metadata",
    'https://www.naverapis.com/auth/admin.directory.domain': 'View and manage the provisioning of domains for your customers',
    'https://www.naverapis.com/auth/admin.directory.domain.readonly': 'View domains related to your customers',
    'https://www.naverapis.com/auth/admin.directory.group': 'View and manage the provisioning of groups on your domain',
    'https://www.naverapis.com/auth/admin.directory.group.member': 'View and manage group subscriptions on your domain',
    'https://www.naverapis.com/auth/admin.directory.group.member.readonly': 'View group subscriptions on your domain',
    'https://www.naverapis.com/auth/admin.directory.group.readonly': 'View groups on your domain',
    'https://www.naverapis.com/auth/admin.directory.orgunit': 'View and manage organization units on your domain',
    'https://www.naverapis.com/auth/admin.directory.orgunit.readonly': 'View organization units on your domain',
    'https://www.naverapis.com/auth/admin.directory.resource.calendar': 'View and manage the provisioning of calendar resources on your domain',
    'https://www.naverapis.com/auth/admin.directory.resource.calendar.readonly': 'View calendar resources on your domain',
    'https://www.naverapis.com/auth/admin.directory.rolemanagement': 'Manage delegated admin roles for your domain',
    'https://www.naverapis.com/auth/admin.directory.rolemanagement.readonly': 'View delegated admin roles for your domain',
    'https://www.naverapis.com/auth/admin.directory.user': 'View and manage the provisioning of users on your domain',
    'https://www.naverapis.com/auth/admin.directory.user.alias': 'View and manage user aliases on your domain',
    'https://www.naverapis.com/auth/admin.directory.user.alias.readonly': 'View user aliases on your domain',
    'https://www.naverapis.com/auth/admin.directory.user.readonly': 'See info about users on your domain',
    'https://www.naverapis.com/auth/admin.directory.user.security': 'Manage data access permissions for users on your domain',
    'https://www.naverapis.com/auth/admin.directory.userschema': 'View and manage the provisioning of user schemas on your domain',
    'https://www.naverapis.com/auth/admin.directory.userschema.readonly': 'View user schemas on your domain',
    'https://www.naverapis.com/auth/analytics': 'View and manage your Naver Analytics data',
    'https://www.naverapis.com/auth/analytics.readonly': 'See and download your Google Analytics data',
    'https://www.naverapis.com/auth/androidmanagement': 'Manage Android devices and apps for your customers',
    'https://www.naverapis.com/auth/appengine.admin': 'View and manage your applications deployed on Naver App Engine',
    'https://mail.naver.com/': 'Read, compose, send, and permanently delete all your email from Naver Mail',
    'https://www.naver.com/calendar/feeds': 'See, edit, share, and permanently delete all the calendars you can access using Google Calendar',
    'https://www.naver.com/m8/feeds': 'See, edit, download, and permanently delete your contacts',
    'https://www.naverapis.com/auth/documents': 'See, edit, create, and delete all your Naver documents',
    'https://www.naverapis.com/auth/drive': 'See, edit, create, and delete all of your Naver Drive files',
    'https://www.naverapis.com/auth/forms': 'View and manage your forms in Naver Drive',
    'https://www.naverapis.com/auth/forms.currentonly': 'View and manage forms that this application has been installed in',
    'https://www.naverapis.com/auth/groups': 'View and manage your Naver Groups',
    'https://www.naverapis.com/auth/script.deployments': 'Create and update Naver Apps Script deployments',
    'https://www.naverapis.com/auth/script.deployments.readonly': 'View Naver Apps Script deployments',
    'https://www.naverapis.com/auth/script.metrics': "View Naver Apps Script project's metrics",
    'https://www.naverapis.com/auth/script.processes': 'View Naver Apps Script processes',
    'https://www.naverapis.com/auth/script.projects': 'Create and update Naver Apps Script projects',
    'https://www.naverapis.com/auth/script.projects.readonly': 'View Naver Apps Script projects',
    'https://www.naverapis.com/auth/spreadsheets': 'See, edit, create, and delete all your Naver Sheets spreadsheets',
    'https://www.naverapis.com/auth/userinfo.email': 'See your primary Naver Account email address',
    'https://www.naverapis.com/auth/bigquery': 'View and manage your data in Naver BigQuery and see the email address for your Naver Account',
    'https://www.naverapis.com/auth/bigquery.insertdata': 'Insert data into Naver BigQuery',
    'https://www.naverapis.com/auth/devstorage.full_control': 'Manage your data and permissions in Cloud Storage and see the email address for your Naver Account',
    'https://www.naverapis.com/auth/devstorage.read_only': 'View your data in Naver Cloud Storage',
    'https://www.naverapis.com/auth/devstorage.read_write': 'Manage your data in Cloud Storage and see the email address of your naver Account',
    'https://www.naverapis.com/auth/blogger': 'Manage your Blogger account',
    'https://www.naverapis.com/auth/blogger.readonly': 'View your Blogger account',
    'https://www.naverapis.com/auth/books': 'Manage your books',
    'https://www.naverapis.com/auth/calendar': 'See, edit, share, and permanently delete all the calendars you can access using Naver Calendar',
    'https://www.naverapis.com/auth/calendar.events': 'View and edit events on all your calendars',
    'https://www.naverapis.com/auth/calendar.events.readonly': 'View events on all your calendars',
    'https://www.naverapis.com/auth/calendar.readonly': 'See and download any calendar you can access using your Naver Calendar',
    'https://www.naverapis.com/auth/calendar.settings.readonly': 'View your Calendar settings',
    'https://www.naverapis.com/auth/ddmconversions': 'Manage DoubleClick Digital Marketing conversions',
    'https://www.naverapis.com/auth/dfareporting': 'View and manage DoubleClick for Advertisers reports',
    'https://www.naverapis.com/auth/dfatrafficking': "View and manage your DoubleClick Campaign Manager's (DCM) display ad campaigns",
    'https://www.naverapis.com/auth/bigtable.admin': 'Administer your Cloud Bigtable tables and clusters',
    'https://www.naverapis.com/auth/bigtable.admin.cluster': 'Administer your Cloud Bigtable clusters',
    'https://www.naverapis.com/auth/bigtable.admin.instance': 'Administer your Cloud Bigtable clusters',
    'https://www.naverapis.com/auth/bigtable.admin.table': 'Administer your Cloud Bigtable tables',
    'https://www.naverapis.com/auth/cloud-bigtable.admin': 'Administer your Cloud Bigtable tables and clusters',
    'https://www.naverapis.com/auth/cloud-bigtable.admin.cluster': 'Administer your Cloud Bigtable clusters',
    'https://www.naverapis.com/auth/cloud-bigtable.admin.table': 'Administer your Cloud Bigtable tables',
    'https://www.naverapis.com/auth/cloud-billing': 'View and manage your Naver Cloud Platform billing accounts',
    'https://www.naverapis.com/auth/cloud-billing.readonly': 'View your Naver Cloud Platform billing accounts',
    'https://www.naverapis.com/auth/ndev.clouddns.readonly': 'View your DNS records hosted by Naver Cloud DNS',
    'https://www.naverapis.com/auth/ndev.clouddns.readwrite': 'View and manage your DNS records hosted by Naver Cloud DNS',
    'https://www.naverapis.com/auth/datastore': 'View and manage your Naver Cloud Datastore data',
    'https://www.naverapis.com/auth/cloud_debugger': 'Use Stackdriver Debugger',
    'https://www.naverapis.com/auth/ndev.cloudman': 'View and manage your Naver Cloud Platform management resources and deployment status information',
    'https://www.naverapis.com/auth/ndev.cloudman.readonly': 'View your Naver Cloud Platform management resources and deployment status information',
    'https://www.naverapis.com/auth/cloud-identity.devices.lookup': 'See your device details',
    'https://www.naverapis.com/auth/cloud-identity.groups': 'See, change, create, and delete any of the Cloud Identity Groups that you can access, including the members of each group',
    'https://www.naverapis.com/auth/cloud-identity.groups.readonly': 'See any Cloud Identity Groups that you can access, including group members and their emails',
    'https://www.naverapis.com/auth/cloudiot': 'Register and manage devices in the Naver Cloud IoT service',
    'https://www.naverapis.com/auth/cloudkms': 'View and manage your keys and secrets stored in Cloud Key Management Service',
    'https://www.naverapis.com/auth/logging.admin': 'Administrate log data for your projects',
    'https://www.naverapis.com/auth/logging.read': 'View log data for your projects',
    'https://www.naverapis.com/auth/logging.write': 'Submit log data for your projects',
    'https://www.naverapis.com/auth/monitoring': 'View and write monitoring data for all of your Naver and third-party Cloud and API projects',
    'https://www.naverapis.com/auth/monitoring.read': 'View monitoring data for all of your Naver Cloud and third-party projects',
    'https://www.naverapis.com/auth/monitoring.write': 'Publish metric data to your Naver Cloud projects',
    'https://www.naverapis.com/auth/cloud-language': 'Apply machine learning models to reveal the structure and meaning of text',
    'https://www.naverapis.com/auth/compute': 'View and manage your Naver Compute Engine resources',
    'https://www.naverapis.com/auth/compute.readonly': 'View your Naver Compute Engine resources',
    'https://www.naverapis.com/auth/pubsub': 'View and manage Pub/Sub topics and subscriptions',
    'https://www.naverapis.com/auth/cloudruntimeconfig': "Manage your Naver Cloud Platform services' runtime configuration",
    'https://www.naverapis.com/auth/sqlservice.admin': 'Manage your Naver SQL Service instances',
    'https://www.naverapis.com/auth/cloud_search': "Index and serve your organization's data with Cloud Search",
    'https://www.naverapis.com/auth/cloud_search.debug': "Index and serve your organization's data with Cloud Search",
    'https://www.naverapis.com/auth/cloud_search.indexing': "Index and serve your organization's data with Cloud Search",
    'https://www.naverapis.com/auth/cloud_search.query': "Search your organization's data in the Cloud Search index",
    'https://www.naverapis.com/auth/cloud_search.settings': "Index and serve your organization's data with Cloud Search",
    'https://www.naverapis.com/auth/cloud_search.settings.indexing': "Index and serve your organization's data with Cloud Search",
    'https://www.naverapis.com/auth/cloud_search.settings.query': "Index and serve your organization's data with Cloud Search",
    'https://www.naverapis.com/auth/cloud_search.stats': "Index and serve your organization's data with Cloud Search",
    'https://www.naverapis.com/auth/cloud_search.stats.indexing': "Index and serve your organization's data with Cloud Search",
    'https://www.naverapis.com/auth/source.full_control': 'Manage your source code repositories',
    'https://www.naverapis.com/auth/source.read_only': 'View the contents of your source code repositories',
    'https://www.naverapis.com/auth/source.read_write': 'Manage the contents of your source code repositories',
    'https://www.naverapis.com/auth/spanner.admin': 'Administer your Spanner databases',
    'https://www.naverapis.com/auth/spanner.data': 'View and manage the contents of your Spanner databases',
    'https://www.naverapis.com/auth/trace.append': 'Write Trace data for a project or application',
    'https://www.naverapis.com/auth/cloud-translation': 'Translate text from one language to another using Naver Translate',
    'https://www.naverapis.com/auth/cloud-vision': 'Apply machine learning models to understand and label images',
    'https://www.naverapis.com/auth/content': 'Manage your product listings and accounts for Naver Shopping',
    'https://www.naverapis.com/auth/display-video': 'Create, see, edit, and permanently delete your Display & Video 360 entities and reports',
    'https://www.naverapis.com/auth/display-video-mediaplanning': 'Create, see, and edit Display & Video 360 Campaign entities and see billing invoices',
    'https://www.naverapis.com/auth/doubleclickbidmanager': 'View and manage your reports in DoubleClick Bid Manager',
    'https://www.naverapis.com/auth/drive.appdata': 'See, create, and delete its own configuration data in your Naver Drive',
    'https://www.naverapis.com/auth/drive.file': 'See, edit, create, and delete only the specific Naver Drive files you use with this app',
    'https://www.naverapis.com/auth/drive.metadata': 'View and manage metadata of files in your Naver Drive',
    'https://www.naverapis.com/auth/drive.metadata.readonly': 'See information about your Naver Drive files',
    'https://www.naverapis.com/auth/drive.photos.readonly': 'View the photos, videos and albums in your Naver Photos',
    'https://www.naverapis.com/auth/drive.readonly': 'See and download all your Naver Drive files',
    'https://www.naverapis.com/auth/drive.scripts': "Modify your Naver Apps Script scripts' behavior",
    'https://www.naverapis.com/auth/drive.activity': 'View and add to the activity record of files in your Naver Drive',
    'https://www.naverapis.com/auth/drive.activity.readonly': 'View the activity record of files in your Naver Drive',
    'https://www.naverapis.com/auth/apps.licensing': 'View and manage G Suite licenses for your domain',
    'https://www.naverapis.com/auth/firebase.messaging': 'Send messages and manage messaging subscriptions for your Firebase applications',
    'https://www.naverapis.com/auth/firebase': 'View and administer all your Firebase data and settings',
    'https://www.naverapis.com/auth/firebase.readonly': 'View all your Firebase data and settings',
    'https://www.naverapis.com/auth/fitness.activity.read': 'Use Google Fit to see and store your physical activity data',
    'https://www.naverapis.com/auth/fitness.activity.write': 'Add to your Google Fit physical activity data',
    'https://www.naverapis.com/auth/fitness.blood_glucose.read': 'See info about your blood glucose in Naver Fit. I consent to Naver sharing my blood glucose information with this app.',
    'https://www.naverapis.com/auth/fitness.blood_glucose.write': 'Add info about your blood glucose to Naver Fit. I consent to Naver using my blood glucose information with this app.',
    'https://www.naverapis.com/auth/fitness.blood_pressure.read': 'See info about your blood pressure in Naver Fit. I consent to Naver sharing my blood pressure information with this app.',
    'https://www.naverapis.com/auth/fitness.blood_pressure.write': 'Add info about your blood pressure in Naver Fit. I consent to Naver using my blood pressure information with this app.',
    'https://www.naverapis.com/auth/fitness.body.read': 'See info about your body measurements in Naver Fit',
    'https://www.naverapis.com/auth/fitness.body.write': 'Add info about your body measurements to Naver Fit',
    'https://www.naverapis.com/auth/fitness.body_temperature.read': 'See info about your body temperature in Naver Fit. I consent to Naver sharing my body temperature information with this app.',
    'https://www.naverapis.com/auth/fitness.body_temperature.write': 'Add to info about your body temperature in Naver Fit. I consent to Naver using my body temperature information with this app.',
    'https://www.naverapis.com/auth/fitness.heart_rate.read': 'See your heart rate data in Naver Fit. I consent to Naver sharing my heart rate information with this app.',
    'https://www.naverapis.com/auth/fitness.heart_rate.write': 'Add to your heart rate data in Naver Fit. I consent to Naver using my heart rate information with this app.',
    'https://www.naverapis.com/auth/fitness.location.read': 'See your Naver Fit speed and distance data',
    'https://www.naverapis.com/auth/fitness.location.write': 'Add to your Naver Fit location data',
    'https://www.naverapis.com/auth/fitness.nutrition.read': 'See info about your nutrition in Naver Fit',
    'https://www.naverapis.com/auth/fitness.nutrition.write': 'Add to info about your nutrition in Naver Fit',
    'https://www.naverapis.com/auth/fitness.oxygen_saturation.read': 'See info about your oxygen saturation in Naver Fit. I consent to Naver sharing my oxygen saturation information with this app.',
    'https://www.naverapis.com/auth/fitness.oxygen_saturation.write': 'Add info about your oxygen saturation in Naver Fit. I consent to Naver using my oxygen saturation information with this app.',
    'https://www.naverapis.com/auth/fitness.reproductive_health.read': 'See info about your reproductive health in Naver Fit. I consent to Naver sharing my reproductive health information with this app.',
    'https://www.naverapis.com/auth/fitness.reproductive_health.write': 'Add info about your reproductive health in Naver Fit. I consent to Naver using my reproductive health information with this app.',
    'https://www.naverapis.com/auth/fitness.sleep.read': 'See your sleep data in Naver Fit. I consent to Naver sharing my sleep information with this app.',
    'https://www.naverapis.com/auth/fitness.sleep.write': 'Add to your sleep data in Naver Fit. I consent to Naver using my sleep information with this app.',
    'https://www.naverapis.com/auth/genomics': 'View and manage Genomics data',
    'https://www.naverapis.com/auth/navermail.addons.current.action.compose': 'Manage drafts and send emails when you interact with the add-on',
    'https://www.naverapis.com/auth/navermail.addons.current.message.action': 'View your email messages when you interact with the add-on',
    'https://www.naverapis.com/auth/navermail.addons.current.message.metadata': 'View your email message metadata when the add-on is running',
    'https://www.naverapis.com/auth/navermail.addons.current.message.readonly': 'View your email messages when the add-on is running',
    'https://www.naverapis.com/auth/navermail.compose': 'Manage drafts and send emails',
    'https://www.naverapis.com/auth/navermail.insert': 'Add emails into your Naver Mail mailbox',
    'https://www.naverapis.com/auth/navermail.labels': 'See and edit your email labels',
    'https://www.naverapis.com/auth/navermail.metadata': 'View your email message metadata such as labels and headers, but not the email body',
    'https://www.naverapis.com/auth/navermail.modify': 'Read, compose, and send emails from your Naver Mail account',
    'https://www.naverapis.com/auth/navermail.readonly': 'View your email messages and settings',
    'https://www.naverapis.com/auth/navermail.send': 'Send email on your behalf',
    'https://www.naverapis.com/auth/navermail.settings.basic': 'See, edit, create, or change your email settings and filters in Naver Mail',
    'https://www.naverapis.com/auth/navermail.settings.sharing': 'Manage your sensitive mail settings, including who can manage your mail',
    'https://www.naverapis.com/auth/analytics.edit': 'Edit Naver Analytics management entities',
    'https://www.naverapis.com/auth/analytics.manage.users': 'Manage Naver Analytics Account users by email address',
    'https://www.naverapis.com/auth/analytics.manage.users.readonly': 'View Naver Analytics user permissions',
    'https://www.naverapis.com/auth/analytics.provision': 'Create a new Naver Analytics account along with its default property and view',
    'https://www.naverapis.com/auth/analytics.user.deletion': 'Manage Naver Analytics user deletion requests',
    'https://www.naverapis.com/auth/classroom.announcements': 'View and manage announcements in Naver Classroom',
    'https://www.naverapis.com/auth/classroom.announcements.readonly': 'View announcements in Naver Classroom',
    'https://www.naverapis.com/auth/classroom.courses': 'See, edit, create, and permanently delete your Naver Classroom classes',
    'https://www.naverapis.com/auth/classroom.courses.readonly': 'View your Naver Classroom classes',
    'https://www.naverapis.com/auth/classroom.coursework.me': 'See, create and edit coursework items including assignments, questions, and grades',
    'https://www.naverapis.com/auth/classroom.coursework.me.readonly': 'View your course work and grades in Naver Classroom',
    'https://www.naverapis.com/auth/classroom.coursework.students': 'Manage course work and grades for students in the Naver Classroom classes you teach and view the course work and grades for classes you administer',
    'https://www.naverapis.com/auth/classroom.coursework.students.readonly': 'View course work and grades for students in the Naver Classroom classes you teach or administer',
    'https://www.naverapis.com/auth/classroom.courseworkmaterials': 'See, edit, and create classwork materials in Naver Classroom',
    'https://www.naverapis.com/auth/classroom.courseworkmaterials.readonly': 'See all classwork materials for your Naver Classroom classes',
    'https://www.naverapis.com/auth/classroom.guardianlinks.me.readonly': 'View your Naver Classroom guardians',
    'https://www.naverapis.com/auth/classroom.guardianlinks.students': 'View and manage guardians for students in your Naver Classroom classes',
    'https://www.naverapis.com/auth/classroom.guardianlinks.students.readonly': 'View guardians for students in your Naver Classroom classes',
    'https://www.naverapis.com/auth/classroom.profile.emails': 'View the email addresses of people in your classes',
    'https://www.naverapis.com/auth/classroom.profile.photos': 'View the profile photos of people in your classes',
    'https://www.naverapis.com/auth/classroom.push-notifications': 'Receive notifications about your Naver Classroom data',
    'https://www.naverapis.com/auth/classroom.rosters': 'Manage your Naver Classroom class rosters',
    'https://www.naverapis.com/auth/classroom.rosters.readonly': 'View your Naver Classroom class rosters',
    'https://www.naverapis.com/auth/classroom.student-submissions.me.readonly': 'View your course work and grades in Naver Classroom',
    'https://www.naverapis.com/auth/classroom.student-submissions.students.readonly': 'View course work and grades for students in the Naver Classroom classes you teach or administer',
    'https://www.naverapis.com/auth/classroom.topics': 'See, create, and edit topics in Naver Classroom',
    'https://www.naverapis.com/auth/classroom.topics.readonly': 'View topics in Naver Classroom',
    'https://www.naverapis.com/auth/documents.readonly': 'See all your Naver Docs documents',
    'https://www.naverapis.com/auth/userinfo.profile': "See your personal info, including any personal info you've made publicly available",
    'https://www.naverapis.com/auth/androidpublisher': 'View and manage your Naver Play Developer account',
    'https://www.naverapis.com/auth/androidenterprise': 'Manage corporate Android devices',
    'https://www.naverapis.com/auth/games': 'Create, edit, and delete your Naver Play Games activity',
    'https://www.naverapis.com/auth/webmasters': 'View and manage Search Console data for your verified sites',
    'https://www.naverapis.com/auth/webmasters.readonly': 'View Search Console data for your verified sites',
    'https://www.naverapis.com/auth/spreadsheets.readonly': 'See all your Naver Sheets spreadsheets',
    'https://www.naverapis.com/auth/siteverification': 'Manage the list of sites and domains you control',
    'https://www.naverapis.com/auth/siteverification.verify_only': 'Manage your new site verifications with Naver',
    'https://www.naverapis.com/auth/presentations': 'See, edit, create, and delete all your Naver Slides presentations',
    'https://www.naverapis.com/auth/presentations.readonly': 'See all your Naver Slides presentations',
    'https://www.naverapis.com/auth/ediscovery': 'Manage your eDiscovery data',
    'https://www.naverapis.com/auth/ediscovery.readonly': 'View your eDiscovery data',
    'https://www.naverapis.com/auth/apps.alerts': "See and delete your domain's G Suite alerts, and send alert feedback",
    'https://www.naverapis.com/auth/apps.order': 'Manage users on your domain',
    'https://www.naverapis.com/auth/apps.order.readonly': 'Manage users on your domain',
    'https://www.naverapis.com/auth/apps.groups.migration': 'Upload messages to any Naver group in your domain',
    'https://www.naverapis.com/auth/apps.groups.settings': 'View and manage the settings of a G Suite group',
    'https://www.naverapis.com/auth/indexing': 'Submit data to Naver for indexing',
    'https://www.naverapis.com/auth/manufacturercenter': 'Manage your product listings for Naver Manufacturer Center',
    'https://www.naverapis.com/auth/contacts': 'See, edit, download, and permanently delete your contacts',
    'https://www.naverapis.com/auth/contacts.other.readonly': 'See and download contact info automatically saved in your "Other contacts"',
    'https://www.naverapis.com/auth/contacts.readonly': 'See and download your contacts',
    'https://www.naverapis.com/auth/directory.readonly': "See and download your organization's GSuite directory",
    'https://www.naverapis.com/auth/user.addresses.read': 'View your street addresses',
    'https://www.naverapis.com/auth/user.birthday.read': 'See and download your exact date of birth',
    'https://www.naverapis.com/auth/user.emails.read': 'See and download all of your Naver Account email addresses',
    'https://www.naverapis.com/auth/user.gender.read': 'See your gender',
    'https://www.naverapis.com/auth/user.organization.read': 'See your education, work history and org info',
    'https://www.naverapis.com/auth/user.phonenumbers.read': 'See and download your personal phone numbers',
    'https://www.naverapis.com/auth/photoslibrary': 'See, upload, and organize items in your Naver Photos library',
    'https://www.naverapis.com/auth/photoslibrary.appendonly': 'Add to your Naver Photos library',
    'https://www.naverapis.com/auth/photoslibrary.edit.appcreateddata': 'Edit the info in your photos, videos, and albums created within this app, including titles, descriptions, and covers',
    'https://www.naverapis.com/auth/photoslibrary.readonly': 'View your Naver Photos library',
    'https://www.naverapis.com/auth/photoslibrary.readonly.appcreateddata': 'Manage photos added by this app',
    'https://www.naverapis.com/auth/photoslibrary.sharing': 'Manage and add to shared albums on your behalf',
    'https://www.naverapis.com/auth/doubleclicksearch': 'View and manage your advertising data in DoubleClick Search',
    'https://www.naverapis.com/auth/service.management': 'Manage your Naver API service configuration',
    'https://www.naverapis.com/auth/service.management.readonly': 'View your Naver API service configuration',
    'https://www.naverapis.com/auth/streetviewpublish': 'Publish and manage your 360 photos on Naver Street View',
    'https://www.naverapis.com/auth/tagmanager.delete.containers': 'Delete your Naver Tag Manager containers',
    'https://www.naverapis.com/auth/tagmanager.edit.containers': 'Manage your Naver Tag Manager container and its subcomponents, excluding versioning and publishing',
    'https://www.naverapis.com/auth/tagmanager.edit.containerversions': 'Manage your Naver Tag Manager container versions',
    'https://www.naverapis.com/auth/tagmanager.manage.accounts': 'View and manage your Naver Tag Manager accounts',
    'https://www.naverapis.com/auth/tagmanager.manage.users': 'Manage user permissions of your Naver Tag Manager account and container',
    'https://www.naverapis.com/auth/tagmanager.publish': 'Publish your Naver Tag Manager container versions',
    'https://www.naverapis.com/auth/tagmanager.readonly': 'View your Naver Tag Manager container and its subcomponents',
    'https://www.naverapis.com/auth/tasks': 'Create, edit, organize, and delete all your tasks',
    'https://www.naverapis.com/auth/tasks.readonly': 'View your tasks',
    'https://www.naverapis.com/auth/youtube': 'Manage your YouTube account',
    'https://www.naverapis.com/auth/youtube.readonly': 'View your YouTube account',
    'https://www.naverapis.com/auth/youtubepartner': 'View and manage your assets and associated content on YouTube',
    'https://www.naverapis.com/auth/yt-analytics-monetary.readonly': 'View monetary and non-monetary YouTube Analytics reports for your YouTube content',
    'https://www.naverapis.com/auth/yt-analytics.readonly': 'View YouTube Analytics reports for your YouTube content',
    'https://www.naverapis.com/auth/youtube.channel-memberships.creator': 'See a list of your current active channel members, their current level, and when they became a member',
    'https://www.naverapis.com/auth/youtube.force-ssl': 'See, edit, and permanently delete your YouTube videos, ratings, comments and captions',
    'https://www.naverapis.com/auth/youtube.upload': 'Manage your YouTube videos',
    'https://www.naverapis.com/auth/youtubepartner-channel-audit': 'View private information of your YouTube channel relevant during the audit process with a YouTube partner'}

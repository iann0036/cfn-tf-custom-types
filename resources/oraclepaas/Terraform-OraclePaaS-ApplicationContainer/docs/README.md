# Terraform::OraclePaaS::ApplicationContainer

The `oraclepaas_application_container` resource creates and manages an Application Container.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OraclePaaS::ApplicationContainer",
    "Properties" : {
        "<a href="#archiveurl" title="ArchiveUrl">ArchiveUrl</a>" : <i>String</i>,
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>[ String, ... ]</i>,
        "<a href="#deploymentfile" title="DeploymentFile">DeploymentFile</a>" : <i>String</i>,
        "<a href="#gitpassword" title="GitPassword">GitPassword</a>" : <i>String</i>,
        "<a href="#gitrepository" title="GitRepository">GitRepository</a>" : <i>String</i>,
        "<a href="#gitusername" title="GitUsername">GitUsername</a>" : <i>String</i>,
        "<a href="#loadbalancersubnets" title="LoadBalancerSubnets">LoadBalancerSubnets</a>" : <i>[ String, ... ]</i>,
        "<a href="#manifestfile" title="ManifestFile">ManifestFile</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#notificationemail" title="NotificationEmail">NotificationEmail</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>[ <a href="runtime.md">Runtime</a>, ... ]</i>,
        "<a href="#subscriptiontype" title="SubscriptionType">SubscriptionType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#deployment" title="Deployment">Deployment</a>" : <i>[ <a href="deployment.md">Deployment</a>, ... ]</i>,
        "<a href="#manifest" title="Manifest">Manifest</a>" : <i>[ <a href="manifest.md">Manifest</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ <a href="services.md">Services</a>, ... ]</i>,
        "<a href="#release" title="Release">Release</a>" : <i>[ <a href="release.md">Release</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OraclePaaS::ApplicationContainer
Properties:
    <a href="#archiveurl" title="ArchiveUrl">ArchiveUrl</a>: <i>String</i>
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>
      - String</i>
    <a href="#deploymentfile" title="DeploymentFile">DeploymentFile</a>: <i>String</i>
    <a href="#gitpassword" title="GitPassword">GitPassword</a>: <i>String</i>
    <a href="#gitrepository" title="GitRepository">GitRepository</a>: <i>String</i>
    <a href="#gitusername" title="GitUsername">GitUsername</a>: <i>String</i>
    <a href="#loadbalancersubnets" title="LoadBalancerSubnets">LoadBalancerSubnets</a>: <i>
      - String</i>
    <a href="#manifestfile" title="ManifestFile">ManifestFile</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#notificationemail" title="NotificationEmail">NotificationEmail</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>
      - <a href="runtime.md">Runtime</a></i>
    <a href="#subscriptiontype" title="SubscriptionType">SubscriptionType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#deployment" title="Deployment">Deployment</a>: <i>
      - <a href="deployment.md">Deployment</a></i>
    <a href="#manifest" title="Manifest">Manifest</a>: <i>
      - <a href="manifest.md">Manifest</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#services" title="Services">Services</a>: <i>
      - <a href="services.md">Services</a></i>
    <a href="#release" title="Release">Release</a>: <i>
      - <a href="release.md">Release</a></i>
</pre>

## Properties

#### ArchiveUrl

Location of the application archive file in Oracle Storage Cloud Service, in the format app-name/file-name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

Uses Oracle Identity Cloud Service to control who can access your Java SE 7 or 8, Node.js, or PHP application. Allowed values are `basic` and `oauth`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityDomain

A list of one or more datacenter locations in the OCI region. Required on OCI.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentFile

The json deployment file containing the attributes related to deploying an application. Use either `deployment_file` or `deployment_attributes` when specifying
deployment information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitPassword

The password for the user with access to the git repository if the repository is private.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitRepository

The URL of the git repository to use the application container.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitUsername

The username of a user with access to the git respository if the repository is private.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSubnets

Two load balancer subnets. Required on OCI.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManifestFile

The json manifest file containing the attributes related to launching an application. Use either `manifest_file` or `manifest_attributes` when specifying
launch information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the existing service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

Comments about the deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmail

Email address to which application deployment status updates are sent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The name of the region where the application container will be deployed. Required on OCI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: No

_Type_: List of <a href="runtime.md">Runtime</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionType

Whether the subscription type is `hourly` or `monthly`. The default is `hourly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags for the application container.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deployment

_Required_: No

_Type_: List of <a href="deployment.md">Deployment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manifest

_Required_: No

_Type_: List of <a href="manifest.md">Manifest</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of <a href="services.md">Services</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Release

_Required_: No

_Type_: List of <a href="release.md">Release</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AppUrl

URL of the created application.

#### WebUrl

Web URL of the application.


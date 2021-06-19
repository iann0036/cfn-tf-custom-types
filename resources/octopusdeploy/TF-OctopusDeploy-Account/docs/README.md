# TF::OctopusDeploy::Account

CloudFormation equivalent of octopusdeploy_account

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OctopusDeploy::Account",
    "Properties" : {
        "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
        "<a href="#accounttype" title="AccountType">AccountType</a>" : <i>String</i>,
        "<a href="#activedirectoryendpointbaseuri" title="ActiveDirectoryEndpointBaseUri">ActiveDirectoryEndpointBaseUri</a>" : <i>String</i>,
        "<a href="#applicationid" title="ApplicationId">ApplicationId</a>" : <i>String</i>,
        "<a href="#authenticationendpoint" title="AuthenticationEndpoint">AuthenticationEndpoint</a>" : <i>String</i>,
        "<a href="#azureenvironment" title="AzureEnvironment">AzureEnvironment</a>" : <i>String</i>,
        "<a href="#certificatedata" title="CertificateData">CertificateData</a>" : <i>String</i>,
        "<a href="#certificatethumbprint" title="CertificateThumbprint">CertificateThumbprint</a>" : <i>String</i>,
        "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#environments" title="Environments">Environments</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#privatekeyfile" title="PrivateKeyFile">PrivateKeyFile</a>" : <i>String</i>,
        "<a href="#privatekeypassphrase" title="PrivateKeyPassphrase">PrivateKeyPassphrase</a>" : <i>String</i>,
        "<a href="#resourcemanagerendpoint" title="ResourceManagerEndpoint">ResourceManagerEndpoint</a>" : <i>String</i>,
        "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
        "<a href="#servicemanagementendpointbaseuri" title="ServiceManagementEndpointBaseUri">ServiceManagementEndpointBaseUri</a>" : <i>String</i>,
        "<a href="#servicemanagementendpointsuffix" title="ServiceManagementEndpointSuffix">ServiceManagementEndpointSuffix</a>" : <i>String</i>,
        "<a href="#spaceid" title="SpaceId">SpaceId</a>" : <i>String</i>,
        "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#tenanttags" title="TenantTags">TenantTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenanteddeploymentparticipation" title="TenantedDeploymentParticipation">TenantedDeploymentParticipation</a>" : <i>String</i>,
        "<a href="#tenants" title="Tenants">Tenants</a>" : <i>[ String, ... ]</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OctopusDeploy::Account
Properties:
    <a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
    <a href="#accounttype" title="AccountType">AccountType</a>: <i>String</i>
    <a href="#activedirectoryendpointbaseuri" title="ActiveDirectoryEndpointBaseUri">ActiveDirectoryEndpointBaseUri</a>: <i>String</i>
    <a href="#applicationid" title="ApplicationId">ApplicationId</a>: <i>String</i>
    <a href="#authenticationendpoint" title="AuthenticationEndpoint">AuthenticationEndpoint</a>: <i>String</i>
    <a href="#azureenvironment" title="AzureEnvironment">AzureEnvironment</a>: <i>String</i>
    <a href="#certificatedata" title="CertificateData">CertificateData</a>: <i>String</i>
    <a href="#certificatethumbprint" title="CertificateThumbprint">CertificateThumbprint</a>: <i>String</i>
    <a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#environments" title="Environments">Environments</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#privatekeyfile" title="PrivateKeyFile">PrivateKeyFile</a>: <i>String</i>
    <a href="#privatekeypassphrase" title="PrivateKeyPassphrase">PrivateKeyPassphrase</a>: <i>String</i>
    <a href="#resourcemanagerendpoint" title="ResourceManagerEndpoint">ResourceManagerEndpoint</a>: <i>String</i>
    <a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
    <a href="#servicemanagementendpointbaseuri" title="ServiceManagementEndpointBaseUri">ServiceManagementEndpointBaseUri</a>: <i>String</i>
    <a href="#servicemanagementendpointsuffix" title="ServiceManagementEndpointSuffix">ServiceManagementEndpointSuffix</a>: <i>String</i>
    <a href="#spaceid" title="SpaceId">SpaceId</a>: <i>String</i>
    <a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#tenanttags" title="TenantTags">TenantTags</a>: <i>
      - String</i>
    <a href="#tenanteddeploymentparticipation" title="TenantedDeploymentParticipation">TenantedDeploymentParticipation</a>: <i>String</i>
    <a href="#tenants" title="Tenants">Tenants</a>: <i>
      - String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### AccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveDirectoryEndpointBaseUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureEnvironment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateThumbprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environments

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyPassphrase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceManagerEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceManagementEndpointBaseUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceManagementEndpointSuffix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantedDeploymentParticipation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenants

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


# TF::OctopusDeploy::AzureServiceFabricClusterDeploymentTarget

CloudFormation equivalent of octopusdeploy_azure_service_fabric_cluster_deployment_target

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OctopusDeploy::AzureServiceFabricClusterDeploymentTarget",
    "Properties" : {
        "<a href="#aadclientcredentialsecret" title="AadClientCredentialSecret">AadClientCredentialSecret</a>" : <i>String</i>,
        "<a href="#aadcredentialtype" title="AadCredentialType">AadCredentialType</a>" : <i>String</i>,
        "<a href="#aadusercredentialpassword" title="AadUserCredentialPassword">AadUserCredentialPassword</a>" : <i>String</i>,
        "<a href="#aadusercredentialusername" title="AadUserCredentialUsername">AadUserCredentialUsername</a>" : <i>String</i>,
        "<a href="#certificatestorelocation" title="CertificateStoreLocation">CertificateStoreLocation</a>" : <i>String</i>,
        "<a href="#certificatestorename" title="CertificateStoreName">CertificateStoreName</a>" : <i>String</i>,
        "<a href="#clientcertificatevariable" title="ClientCertificateVariable">ClientCertificateVariable</a>" : <i>String</i>,
        "<a href="#connectionendpoint" title="ConnectionEndpoint">ConnectionEndpoint</a>" : <i>String</i>,
        "<a href="#environments" title="Environments">Environments</a>" : <i>[ String, ... ]</i>,
        "<a href="#healthstatus" title="HealthStatus">HealthStatus</a>" : <i>String</i>,
        "<a href="#isdisabled" title="IsDisabled">IsDisabled</a>" : <i>Boolean</i>,
        "<a href="#machinepolicyid" title="MachinePolicyId">MachinePolicyId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>String</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ String, ... ]</i>,
        "<a href="#securitymode" title="SecurityMode">SecurityMode</a>" : <i>String</i>,
        "<a href="#servercertificatethumbprint" title="ServerCertificateThumbprint">ServerCertificateThumbprint</a>" : <i>String</i>,
        "<a href="#shellname" title="ShellName">ShellName</a>" : <i>String</i>,
        "<a href="#shellversion" title="ShellVersion">ShellVersion</a>" : <i>String</i>,
        "<a href="#spaceid" title="SpaceId">SpaceId</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#statussummary" title="StatusSummary">StatusSummary</a>" : <i>String</i>,
        "<a href="#tenanttags" title="TenantTags">TenantTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenanteddeploymentparticipation" title="TenantedDeploymentParticipation">TenantedDeploymentParticipation</a>" : <i>String</i>,
        "<a href="#tenants" title="Tenants">Tenants</a>" : <i>[ String, ... ]</i>,
        "<a href="#thumbprint" title="Thumbprint">Thumbprint</a>" : <i>String</i>,
        "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>[ <a href="endpointdefinition.md">EndpointDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OctopusDeploy::AzureServiceFabricClusterDeploymentTarget
Properties:
    <a href="#aadclientcredentialsecret" title="AadClientCredentialSecret">AadClientCredentialSecret</a>: <i>String</i>
    <a href="#aadcredentialtype" title="AadCredentialType">AadCredentialType</a>: <i>String</i>
    <a href="#aadusercredentialpassword" title="AadUserCredentialPassword">AadUserCredentialPassword</a>: <i>String</i>
    <a href="#aadusercredentialusername" title="AadUserCredentialUsername">AadUserCredentialUsername</a>: <i>String</i>
    <a href="#certificatestorelocation" title="CertificateStoreLocation">CertificateStoreLocation</a>: <i>String</i>
    <a href="#certificatestorename" title="CertificateStoreName">CertificateStoreName</a>: <i>String</i>
    <a href="#clientcertificatevariable" title="ClientCertificateVariable">ClientCertificateVariable</a>: <i>String</i>
    <a href="#connectionendpoint" title="ConnectionEndpoint">ConnectionEndpoint</a>: <i>String</i>
    <a href="#environments" title="Environments">Environments</a>: <i>
      - String</i>
    <a href="#healthstatus" title="HealthStatus">HealthStatus</a>: <i>String</i>
    <a href="#isdisabled" title="IsDisabled">IsDisabled</a>: <i>Boolean</i>
    <a href="#machinepolicyid" title="MachinePolicyId">MachinePolicyId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>String</i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - String</i>
    <a href="#securitymode" title="SecurityMode">SecurityMode</a>: <i>String</i>
    <a href="#servercertificatethumbprint" title="ServerCertificateThumbprint">ServerCertificateThumbprint</a>: <i>String</i>
    <a href="#shellname" title="ShellName">ShellName</a>: <i>String</i>
    <a href="#shellversion" title="ShellVersion">ShellVersion</a>: <i>String</i>
    <a href="#spaceid" title="SpaceId">SpaceId</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#statussummary" title="StatusSummary">StatusSummary</a>: <i>String</i>
    <a href="#tenanttags" title="TenantTags">TenantTags</a>: <i>
      - String</i>
    <a href="#tenanteddeploymentparticipation" title="TenantedDeploymentParticipation">TenantedDeploymentParticipation</a>: <i>String</i>
    <a href="#tenants" title="Tenants">Tenants</a>: <i>
      - String</i>
    <a href="#thumbprint" title="Thumbprint">Thumbprint</a>: <i>String</i>
    <a href="#uri" title="Uri">Uri</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>
      - <a href="endpointdefinition.md">EndpointDefinition</a></i>
</pre>

## Properties

#### AadClientCredentialSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadCredentialType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadUserCredentialPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadUserCredentialUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateStoreLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateStoreName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateVariable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionEndpoint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environments

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachinePolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateThumbprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShellName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShellVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusSummary

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

#### Thumbprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: No

_Type_: List of <a href="endpointdefinition.md">EndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### HasLatestCalamari

Returns the <code>HasLatestCalamari</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsInProcess

Returns the <code>IsInProcess</code> value.


# TF::OCI::BlockchainBlockchainPlatform

This resource provides the Blockchain Platform resource in Oracle Cloud Infrastructure Blockchain service.

Creates a new Blockchain Platform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::BlockchainBlockchainPlatform",
    "Properties" : {
        "<a href="#cacertarchivetext" title="CaCertArchiveText">CaCertArchiveText</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#computeshape" title="ComputeShape">ComputeShape</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#federateduserid" title="FederatedUserId">FederatedUserId</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#idcsaccesstoken" title="IdcsAccessToken">IdcsAccessToken</a>" : <i>String</i>,
        "<a href="#isbyol" title="IsByol">IsByol</a>" : <i>Boolean</i>,
        "<a href="#loadbalancershape" title="LoadBalancerShape">LoadBalancerShape</a>" : <i>String</i>,
        "<a href="#platformrole" title="PlatformRole">PlatformRole</a>" : <i>String</i>,
        "<a href="#storagesizeintbs" title="StorageSizeInTbs">StorageSizeInTbs</a>" : <i>Double</i>,
        "<a href="#totalocpucapacity" title="TotalOcpuCapacity">TotalOcpuCapacity</a>" : <i>Double</i>,
        "<a href="#replicas" title="Replicas">Replicas</a>" : <i>[ <a href="replicasdefinition.md">ReplicasDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::BlockchainBlockchainPlatform
Properties:
    <a href="#cacertarchivetext" title="CaCertArchiveText">CaCertArchiveText</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#computeshape" title="ComputeShape">ComputeShape</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#federateduserid" title="FederatedUserId">FederatedUserId</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#idcsaccesstoken" title="IdcsAccessToken">IdcsAccessToken</a>: <i>String</i>
    <a href="#isbyol" title="IsByol">IsByol</a>: <i>Boolean</i>
    <a href="#loadbalancershape" title="LoadBalancerShape">LoadBalancerShape</a>: <i>String</i>
    <a href="#platformrole" title="PlatformRole">PlatformRole</a>: <i>String</i>
    <a href="#storagesizeintbs" title="StorageSizeInTbs">StorageSizeInTbs</a>: <i>Double</i>
    <a href="#totalocpucapacity" title="TotalOcpuCapacity">TotalOcpuCapacity</a>: <i>Double</i>
    <a href="#replicas" title="Replicas">Replicas</a>: <i>
      - <a href="replicasdefinition.md">ReplicasDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CaCertArchiveText

Base64 encoded text in ASCII character set of a Thirdparty CA Certificates archive file. The Archive file is a zip file containing third part CA Certificates, the ca key and certificate files used when issuing enrollment certificates (ECerts) and transaction certificates (TCerts). The chainfile (if it exists) contains the certificate chain which should be trusted for this CA, where the 1st in the chain is always the root CA certificate. File list in zip file [ca-cert.pem,ca-key.pem,ca-chain.pem(optional)].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) Compartment Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeShape

Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

(Updatable) Platform Instance Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Platform Instance Display name, can be renamed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FederatedUserId

Identifier for a federated user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdcsAccessToken

IDCS access token with Identity Domain Administrator role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsByol

Bring your own license.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerShape

(Updatable) Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformRole

Role of platform - founder or participant.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageSizeInTbs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TotalOcpuCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replicas

_Required_: No

_Type_: List of <a href="replicasdefinition.md">ReplicasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ComponentDetails

Returns the <code>ComponentDetails</code> value.

#### HostOcpuUtilizationInfo

Returns the <code>HostOcpuUtilizationInfo</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsMultiAd

Returns the <code>IsMultiAd</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### PlatformShapeType

Returns the <code>PlatformShapeType</code> value.

#### ServiceEndpoint

Returns the <code>ServiceEndpoint</code> value.

#### ServiceVersion

Returns the <code>ServiceVersion</code> value.

#### State

Returns the <code>State</code> value.

#### StorageUsedInTbs

Returns the <code>StorageUsedInTbs</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.


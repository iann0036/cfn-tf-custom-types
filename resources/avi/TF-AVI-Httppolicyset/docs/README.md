# TF::AVI::Httppolicyset

The HTTPPolicySet resource allows the creation and management of Avi HTTPPolicySet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Httppolicyset",
    "Properties" : {
        "<a href="#cloudconfigcksum" title="CloudConfigCksum">CloudConfigCksum</a>" : <i>String</i>,
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipreputationdbref" title="IpReputationDbRef">IpReputationDbRef</a>" : <i>String</i>,
        "<a href="#isinternalpolicy" title="IsInternalPolicy">IsInternalPolicy</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#httprequestpolicy" title="HttpRequestPolicy">HttpRequestPolicy</a>" : <i>[ <a href="httprequestpolicydefinition.md">HttpRequestPolicyDefinition</a>, ... ]</i>,
        "<a href="#httpresponsepolicy" title="HttpResponsePolicy">HttpResponsePolicy</a>" : <i>[ <a href="httpresponsepolicydefinition.md">HttpResponsePolicyDefinition</a>, ... ]</i>,
        "<a href="#httpsecuritypolicy" title="HttpSecurityPolicy">HttpSecurityPolicy</a>" : <i>[ <a href="httpsecuritypolicydefinition.md">HttpSecurityPolicyDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Httppolicyset
Properties:
    <a href="#cloudconfigcksum" title="CloudConfigCksum">CloudConfigCksum</a>: <i>String</i>
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipreputationdbref" title="IpReputationDbRef">IpReputationDbRef</a>: <i>String</i>
    <a href="#isinternalpolicy" title="IsInternalPolicy">IsInternalPolicy</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#httprequestpolicy" title="HttpRequestPolicy">HttpRequestPolicy</a>: <i>
      - <a href="httprequestpolicydefinition.md">HttpRequestPolicyDefinition</a></i>
    <a href="#httpresponsepolicy" title="HttpResponsePolicy">HttpResponsePolicy</a>: <i>
      - <a href="httpresponsepolicydefinition.md">HttpResponsePolicyDefinition</a></i>
    <a href="#httpsecuritypolicy" title="HttpSecurityPolicy">HttpSecurityPolicy</a>: <i>
      - <a href="httpsecuritypolicydefinition.md">HttpSecurityPolicyDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
</pre>

## Properties

#### CloudConfigCksum

Checksum of cloud configuration for pool. Internally set by cloud connector.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBy

Creator name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReputationDbRef

Ip reputation database. It is a reference to an object of type ipreputationdb. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsInternalPolicy

Boolean flag to set is_internal_policy.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the http policy set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestPolicy

_Required_: No

_Type_: List of <a href="httprequestpolicydefinition.md">HttpRequestPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpResponsePolicy

_Required_: No

_Type_: List of <a href="httpresponsepolicydefinition.md">HttpResponsePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpSecurityPolicy

_Required_: No

_Type_: List of <a href="httpsecuritypolicydefinition.md">HttpSecurityPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

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


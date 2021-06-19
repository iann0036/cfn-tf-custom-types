# TF::AWS::FmsPolicy

Provides a resource to create an AWS Firewall Manager policy. You need to be using AWS organizations and have enabled the Firewall Manager administrator account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::FmsPolicy",
    "Properties" : {
        "<a href="#deleteallpolicyresources" title="DeleteAllPolicyResources">DeleteAllPolicyResources</a>" : <i>Boolean</i>,
        "<a href="#excluderesourcetags" title="ExcludeResourceTags">ExcludeResourceTags</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remediationenabled" title="RemediationEnabled">RemediationEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcetags" title="ResourceTags">ResourceTags</a>" : <i>[ <a href="resourcetagsdefinition.md">ResourceTagsDefinition</a>, ... ]</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#resourcetypelist" title="ResourceTypeList">ResourceTypeList</a>" : <i>[ String, ... ]</i>,
        "<a href="#excludemap" title="ExcludeMap">ExcludeMap</a>" : <i>[ <a href="excludemapdefinition.md">ExcludeMapDefinition</a>, ... ]</i>,
        "<a href="#includemap" title="IncludeMap">IncludeMap</a>" : <i>[ <a href="includemapdefinition.md">IncludeMapDefinition</a>, ... ]</i>,
        "<a href="#securityservicepolicydata" title="SecurityServicePolicyData">SecurityServicePolicyData</a>" : <i>[ <a href="securityservicepolicydatadefinition.md">SecurityServicePolicyDataDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::FmsPolicy
Properties:
    <a href="#deleteallpolicyresources" title="DeleteAllPolicyResources">DeleteAllPolicyResources</a>: <i>Boolean</i>
    <a href="#excluderesourcetags" title="ExcludeResourceTags">ExcludeResourceTags</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remediationenabled" title="RemediationEnabled">RemediationEnabled</a>: <i>Boolean</i>
    <a href="#resourcetags" title="ResourceTags">ResourceTags</a>: <i>
      - <a href="resourcetagsdefinition.md">ResourceTagsDefinition</a></i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#resourcetypelist" title="ResourceTypeList">ResourceTypeList</a>: <i>
      - String</i>
    <a href="#excludemap" title="ExcludeMap">ExcludeMap</a>: <i>
      - <a href="excludemapdefinition.md">ExcludeMapDefinition</a></i>
    <a href="#includemap" title="IncludeMap">IncludeMap</a>: <i>
      - <a href="includemapdefinition.md">IncludeMapDefinition</a></i>
    <a href="#securityservicepolicydata" title="SecurityServicePolicyData">SecurityServicePolicyData</a>: <i>
      - <a href="securityservicepolicydatadefinition.md">SecurityServicePolicyDataDefinition</a></i>
</pre>

## Properties

#### DeleteAllPolicyResources

If true, the request will also perform a clean-up process. Defaults to `true`. More information can be found here [AWS Firewall Manager delete policy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeletePolicy.html).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeResourceTags

A boolean value, if true the tags that are specified in the `resource_tags` are not protected by this policy. If set to false and resource_tags are populated, resources that contain tags will be protected by this policy.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The friendly name of the AWS Firewall Manager Policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemediationEnabled

A boolean value, indicates if the policy should automatically applied to resources that already exist in the account.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceTags

A map of resource tags, that if present will filter protections on resources based on the exclude_resource_tags.

_Required_: No

_Type_: List of <a href="resourcetagsdefinition.md">ResourceTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

A resource type to protect. Conflicts with `resource_type_list`. See the [FMS API Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html#fms-Type-Policy-ResourceType) for more information about supported values.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceTypeList

A list of resource types to protect. Conflicts with `resource_type`. See the [FMS API Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html#fms-Type-Policy-ResourceType) for more information about supported values.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeMap

_Required_: No

_Type_: List of <a href="excludemapdefinition.md">ExcludeMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeMap

_Required_: No

_Type_: List of <a href="includemapdefinition.md">IncludeMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityServicePolicyData

_Required_: No

_Type_: List of <a href="securityservicepolicydatadefinition.md">SecurityServicePolicyDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### PolicyUpdateToken

Returns the <code>PolicyUpdateToken</code> value.


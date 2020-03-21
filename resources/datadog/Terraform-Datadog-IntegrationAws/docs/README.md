# Terraform::Datadog::IntegrationAws

Provides a Datadog - Amazon Web Services integration resource. This can be used to create and manage Datadog - Amazon Web Services integration.

Update operations are currently not supported with datadog API so any change forces a new resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::IntegrationAws",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#accountspecificnamespacerules" title="AccountSpecificNamespaceRules">AccountSpecificNamespaceRules</a>" : <i>[ <a href="accountspecificnamespacerules.md">AccountSpecificNamespaceRules</a>, ... ]</i>,
        "<a href="#filtertags" title="FilterTags">FilterTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#hosttags" title="HostTags">HostTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::IntegrationAws
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#accountspecificnamespacerules" title="AccountSpecificNamespaceRules">AccountSpecificNamespaceRules</a>: <i>
      - <a href="accountspecificnamespacerules.md">AccountSpecificNamespaceRules</a></i>
    <a href="#filtertags" title="FilterTags">FilterTags</a>: <i>
      - String</i>
    <a href="#hosttags" title="HostTags">HostTags</a>: <i>
      - String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
</pre>

## Properties

#### AccountId

Your AWS Account ID without dashes.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountSpecificNamespaceRules

Enables or disables metric collection for specific AWS namespaces for this AWS account only. A list of namespaces can be found at the [available namespace rules API endpoint](https://api.datadoghq.com/api/v1/integration/aws/available_namespace_rules).

_Required_: No

_Type_: List of <a href="accountspecificnamespacerules.md">AccountSpecificNamespaceRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterTags

Array of EC2 tags (in the form `key:value`) defines a filter that Datadog use when collecting metrics from EC2. Wildcards, such as `?` (for single characters) and `*` (for multiple characters) can also be used.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostTags

Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

Your Datadog role delegation name.

_Required_: Yes

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

#### ExternalId

Returns the <code>ExternalId</code> value.


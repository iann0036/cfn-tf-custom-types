# TF::LaunchDarkly::FeatureFlag

Provides a LaunchDarkly feature flag resource.

This resource allows you to create and manage feature flags within your LaunchDarkly organization.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::LaunchDarkly::FeatureFlag",
    "Properties" : {
        "<a href="#defaultoffvariation" title="DefaultOffVariation">DefaultOffVariation</a>" : <i>String</i>,
        "<a href="#defaultonvariation" title="DefaultOnVariation">DefaultOnVariation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#includeinsnippet" title="IncludeInSnippet">IncludeInSnippet</a>" : <i>Boolean</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#maintainerid" title="MaintainerId">MaintainerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectkey" title="ProjectKey">ProjectKey</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#temporary" title="Temporary">Temporary</a>" : <i>Boolean</i>,
        "<a href="#variationtype" title="VariationType">VariationType</a>" : <i>String</i>,
        "<a href="#customproperties" title="CustomProperties">CustomProperties</a>" : <i>[ <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>, ... ]</i>,
        "<a href="#variations" title="Variations">Variations</a>" : <i>[ <a href="variationsdefinition.md">VariationsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::LaunchDarkly::FeatureFlag
Properties:
    <a href="#defaultoffvariation" title="DefaultOffVariation">DefaultOffVariation</a>: <i>String</i>
    <a href="#defaultonvariation" title="DefaultOnVariation">DefaultOnVariation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#includeinsnippet" title="IncludeInSnippet">IncludeInSnippet</a>: <i>Boolean</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#maintainerid" title="MaintainerId">MaintainerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectkey" title="ProjectKey">ProjectKey</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#temporary" title="Temporary">Temporary</a>: <i>Boolean</i>
    <a href="#variationtype" title="VariationType">VariationType</a>: <i>String</i>
    <a href="#customproperties" title="CustomProperties">CustomProperties</a>: <i>
      - <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a></i>
    <a href="#variations" title="Variations">Variations</a>: <i>
      - <a href="variationsdefinition.md">VariationsDefinition</a></i>
</pre>

## Properties

#### DefaultOffVariation

The value of the variation served when the flag is off for new environments. Required if `default_on_variation` is set. Flag configurations in existing environments will not be changed. The value used here must be an exact match (including whitespace) to the `value` set in the `variations` list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultOnVariation

The value of the variation served when the flag is on for new environments. Required if `default_off_variation` is set. Flag configurations in existing environments will not be changed. The value used here must be an exact match (including whitespace) to the `value` set in the `variations` list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The feature flag's description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeInSnippet

Specifies whether this flag should be made available to the client-side JavaScript SDK.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The unique feature flag key that references the flag in your application code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintainerId

The feature flag maintainer's 24 character alphanumeric team member ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable name of the feature flag.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectKey

The feature flag's project key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Set of feature flag tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Temporary

Specifies whether the flag is a temporary flag.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VariationType

The feature flag's variation type: `boolean`, `string`, `number` or `json`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProperties

_Required_: No

_Type_: List of <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variations

_Required_: No

_Type_: List of <a href="variationsdefinition.md">VariationsDefinition</a>

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


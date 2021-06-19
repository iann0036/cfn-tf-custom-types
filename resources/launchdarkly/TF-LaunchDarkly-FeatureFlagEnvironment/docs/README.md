# TF::LaunchDarkly::FeatureFlagEnvironment

Provides a LaunchDarkly environment-specific feature flag resource.

This resource allows you to create and manage environment-specific feature flags attributes within your LaunchDarkly organization.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::LaunchDarkly::FeatureFlagEnvironment",
    "Properties" : {
        "<a href="#envkey" title="EnvKey">EnvKey</a>" : <i>String</i>,
        "<a href="#flagid" title="FlagId">FlagId</a>" : <i>String</i>,
        "<a href="#offvariation" title="OffVariation">OffVariation</a>" : <i>Double</i>,
        "<a href="#targetingenabled" title="TargetingEnabled">TargetingEnabled</a>" : <i>Boolean</i>,
        "<a href="#trackevents" title="TrackEvents">TrackEvents</a>" : <i>Boolean</i>,
        "<a href="#flagfallthrough" title="FlagFallthrough">FlagFallthrough</a>" : <i>[ <a href="flagfallthroughdefinition.md">FlagFallthroughDefinition</a>, ... ]</i>,
        "<a href="#prerequisites" title="Prerequisites">Prerequisites</a>" : <i>[ <a href="prerequisitesdefinition.md">PrerequisitesDefinition</a>, ... ]</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rulesdefinition.md">RulesDefinition</a>, ... ]</i>,
        "<a href="#usertargets" title="UserTargets">UserTargets</a>" : <i>[ <a href="usertargetsdefinition.md">UserTargetsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::LaunchDarkly::FeatureFlagEnvironment
Properties:
    <a href="#envkey" title="EnvKey">EnvKey</a>: <i>String</i>
    <a href="#flagid" title="FlagId">FlagId</a>: <i>String</i>
    <a href="#offvariation" title="OffVariation">OffVariation</a>: <i>Double</i>
    <a href="#targetingenabled" title="TargetingEnabled">TargetingEnabled</a>: <i>Boolean</i>
    <a href="#trackevents" title="TrackEvents">TrackEvents</a>: <i>Boolean</i>
    <a href="#flagfallthrough" title="FlagFallthrough">FlagFallthrough</a>: <i>
      - <a href="flagfallthroughdefinition.md">FlagFallthroughDefinition</a></i>
    <a href="#prerequisites" title="Prerequisites">Prerequisites</a>: <i>
      - <a href="prerequisitesdefinition.md">PrerequisitesDefinition</a></i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rulesdefinition.md">RulesDefinition</a></i>
    <a href="#usertargets" title="UserTargets">UserTargets</a>: <i>
      - <a href="usertargetsdefinition.md">UserTargetsDefinition</a></i>
</pre>

## Properties

#### EnvKey

The environment key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlagId

The feature flag's unique `id` in the format `project_key/flag_key`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OffVariation

The index of the variation to serve if targeting is disabled.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetingEnabled

Whether targeting is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrackEvents

Whether to send event data back to LaunchDarkly.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlagFallthrough

_Required_: No

_Type_: List of <a href="flagfallthroughdefinition.md">FlagFallthroughDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prerequisites

_Required_: No

_Type_: List of <a href="prerequisitesdefinition.md">PrerequisitesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rulesdefinition.md">RulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTargets

_Required_: No

_Type_: List of <a href="usertargetsdefinition.md">UserTargetsDefinition</a>

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


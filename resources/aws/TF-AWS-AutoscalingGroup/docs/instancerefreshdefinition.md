# TF::AWS::AutoscalingGroup InstanceRefreshDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#strategy" title="Strategy">Strategy</a>" : <i>String</i>,
    "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ String, ... ]</i>,
    "<a href="#preferences" title="Preferences">Preferences</a>" : <i>[ <a href="preferencesdefinition.md">PreferencesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#strategy" title="Strategy">Strategy</a>: <i>String</i>
<a href="#triggers" title="Triggers">Triggers</a>: <i>
      - String</i>
<a href="#preferences" title="Preferences">Preferences</a>: <i>
      - <a href="preferencesdefinition.md">PreferencesDefinition</a></i>
</pre>

## Properties

#### Strategy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preferences

_Required_: No

_Type_: List of <a href="preferencesdefinition.md">PreferencesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


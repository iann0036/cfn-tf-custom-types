# TF::Kubernetes::LimitRange LimitDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#default" title="Default">Default</a>" : <i>[ <a href="defaultdefinition.md">DefaultDefinition</a>, ... ]</i>,
    "<a href="#defaultrequest" title="DefaultRequest">DefaultRequest</a>" : <i>[ <a href="defaultrequestdefinition.md">DefaultRequestDefinition</a>, ... ]</i>,
    "<a href="#max" title="Max">Max</a>" : <i>[ <a href="maxdefinition.md">MaxDefinition</a>, ... ]</i>,
    "<a href="#maxlimitrequestratio" title="MaxLimitRequestRatio">MaxLimitRequestRatio</a>" : <i>[ <a href="maxlimitrequestratiodefinition.md">MaxLimitRequestRatioDefinition</a>, ... ]</i>,
    "<a href="#min" title="Min">Min</a>" : <i>[ <a href="mindefinition.md">MinDefinition</a>, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#default" title="Default">Default</a>: <i>
      - <a href="defaultdefinition.md">DefaultDefinition</a></i>
<a href="#defaultrequest" title="DefaultRequest">DefaultRequest</a>: <i>
      - <a href="defaultrequestdefinition.md">DefaultRequestDefinition</a></i>
<a href="#max" title="Max">Max</a>: <i>
      - <a href="maxdefinition.md">MaxDefinition</a></i>
<a href="#maxlimitrequestratio" title="MaxLimitRequestRatio">MaxLimitRequestRatio</a>: <i>
      - <a href="maxlimitrequestratiodefinition.md">MaxLimitRequestRatioDefinition</a></i>
<a href="#min" title="Min">Min</a>: <i>
      - <a href="mindefinition.md">MinDefinition</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Default

_Required_: No

_Type_: List of <a href="defaultdefinition.md">DefaultDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRequest

_Required_: No

_Type_: List of <a href="defaultrequestdefinition.md">DefaultRequestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Max

_Required_: No

_Type_: List of <a href="maxdefinition.md">MaxDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLimitRequestRatio

_Required_: No

_Type_: List of <a href="maxlimitrequestratiodefinition.md">MaxLimitRequestRatioDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Min

_Required_: No

_Type_: List of <a href="mindefinition.md">MinDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


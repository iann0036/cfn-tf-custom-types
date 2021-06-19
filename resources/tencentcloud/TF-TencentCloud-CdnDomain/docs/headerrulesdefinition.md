# TF::TencentCloud::CdnDomain HeaderRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headermode" title="HeaderMode">HeaderMode</a>" : <i>String</i>,
    "<a href="#headername" title="HeaderName">HeaderName</a>" : <i>String</i>,
    "<a href="#headervalue" title="HeaderValue">HeaderValue</a>" : <i>String</i>,
    "<a href="#rulepaths" title="RulePaths">RulePaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#headermode" title="HeaderMode">HeaderMode</a>: <i>String</i>
<a href="#headername" title="HeaderName">HeaderName</a>: <i>String</i>
<a href="#headervalue" title="HeaderValue">HeaderValue</a>: <i>String</i>
<a href="#rulepaths" title="RulePaths">RulePaths</a>: <i>
      - String</i>
<a href="#ruletype" title="RuleType">RuleType</a>: <i>String</i>
</pre>

## Properties

#### HeaderMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderValue

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulePaths

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


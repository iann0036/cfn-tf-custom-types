# TF::OPC::LbaasPolicy SetRequestHeaderPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actionwhenheaderexists" title="ActionWhenHeaderExists">ActionWhenHeaderExists</a>" : <i>String</i>,
    "<a href="#actionwhenheadervalueis" title="ActionWhenHeaderValueIs">ActionWhenHeaderValueIs</a>" : <i>[ String, ... ]</i>,
    "<a href="#actionwhenheadervalueisnot" title="ActionWhenHeaderValueIsNot">ActionWhenHeaderValueIsNot</a>" : <i>[ String, ... ]</i>,
    "<a href="#headername" title="HeaderName">HeaderName</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#actionwhenheaderexists" title="ActionWhenHeaderExists">ActionWhenHeaderExists</a>: <i>String</i>
<a href="#actionwhenheadervalueis" title="ActionWhenHeaderValueIs">ActionWhenHeaderValueIs</a>: <i>
      - String</i>
<a href="#actionwhenheadervalueisnot" title="ActionWhenHeaderValueIsNot">ActionWhenHeaderValueIsNot</a>: <i>
      - String</i>
<a href="#headername" title="HeaderName">HeaderName</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### ActionWhenHeaderExists

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionWhenHeaderValueIs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionWhenHeaderValueIsNot

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


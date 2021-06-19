# TF::Volterra::ServicePolicyRule PathDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exactvalues" title="ExactValues">ExactValues</a>" : <i>[ String, ... ]</i>,
    "<a href="#prefixvalues" title="PrefixValues">PrefixValues</a>" : <i>[ String, ... ]</i>,
    "<a href="#regexvalues" title="RegexValues">RegexValues</a>" : <i>[ String, ... ]</i>,
    "<a href="#transformers" title="Transformers">Transformers</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exactvalues" title="ExactValues">ExactValues</a>: <i>
      - String</i>
<a href="#prefixvalues" title="PrefixValues">PrefixValues</a>: <i>
      - String</i>
<a href="#regexvalues" title="RegexValues">RegexValues</a>: <i>
      - String</i>
<a href="#transformers" title="Transformers">Transformers</a>: <i>
      - String</i>
</pre>

## Properties

#### ExactValues

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixValues

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegexValues

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transformers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


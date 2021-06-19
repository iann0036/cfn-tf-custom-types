# TF::Limelight::Delivery ProtocolSetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#publishedprotocol" title="PublishedProtocol">PublishedProtocol</a>" : <i>String</i>,
    "<a href="#sourceport" title="SourcePort">SourcePort</a>" : <i>Double</i>,
    "<a href="#sourceprotocol" title="SourceProtocol">SourceProtocol</a>" : <i>String</i>,
    "<a href="#option" title="Option">Option</a>" : <i>[ <a href="optiondefinition.md">OptionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#publishedprotocol" title="PublishedProtocol">PublishedProtocol</a>: <i>String</i>
<a href="#sourceport" title="SourcePort">SourcePort</a>: <i>Double</i>
<a href="#sourceprotocol" title="SourceProtocol">SourceProtocol</a>: <i>String</i>
<a href="#option" title="Option">Option</a>: <i>
      - <a href="optiondefinition.md">OptionDefinition</a></i>
</pre>

## Properties

#### PublishedProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option

_Required_: No

_Type_: List of <a href="optiondefinition.md">OptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


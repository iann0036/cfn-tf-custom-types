# TF::AVI::Authprofile UserBindDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dntemplate" title="DnTemplate">DnTemplate</a>" : <i>String</i>,
    "<a href="#token" title="Token">Token</a>" : <i>String</i>,
    "<a href="#userattributes" title="UserAttributes">UserAttributes</a>" : <i>[ String, ... ]</i>,
    "<a href="#useridattribute" title="UserIdAttribute">UserIdAttribute</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dntemplate" title="DnTemplate">DnTemplate</a>: <i>String</i>
<a href="#token" title="Token">Token</a>: <i>String</i>
<a href="#userattributes" title="UserAttributes">UserAttributes</a>: <i>
      - String</i>
<a href="#useridattribute" title="UserIdAttribute">UserIdAttribute</a>: <i>String</i>
</pre>

## Properties

#### DnTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


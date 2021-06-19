# TF::ILert::Connection GithubDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
    "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
    "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
<a href="#owner" title="Owner">Owner</a>: <i>String</i>
<a href="#repository" title="Repository">Repository</a>: <i>String</i>
</pre>

## Properties

#### Labels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


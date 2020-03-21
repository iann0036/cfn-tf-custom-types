# Terraform::AWS::AppmeshRoute Header

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#invert" title="Invert">Invert</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#match" title="Match">Match</a>" : <i>[ &lt;a href=&#34;header-match.md&#34;&gt;Match&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#invert" title="Invert">Invert</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#match" title="Match">Match</a>: <i>
      - &lt;a href=&#34;header-match.md&#34;&gt;Match&lt;/a&gt;</i>
</pre>

## Properties

#### Invert

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No
_Type_: List of &lt;a href=&#34;header-match.md&#34;&gt;Match&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


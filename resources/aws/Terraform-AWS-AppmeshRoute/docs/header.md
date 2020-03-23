# Terraform::AWS::AppmeshRoute Header

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#invert" title="Invert">Invert</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#match" title="Match">Match</a>" : <i>[ <a href="header-match.md">Match</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#invert" title="Invert">Invert</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#match" title="Match">Match</a>: <i>
      - <a href="header-match.md">Match</a></i>
</pre>

## Properties

#### Invert

If `true`, the match is on the opposite of the `match` method and value. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the HTTP header in the client request that will be matched on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of <a href="header-match.md">Match</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


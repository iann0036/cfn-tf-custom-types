# Terraform::AWS::AppmeshRoute HttpRoute

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="httproute-action.md">Action</a>, ... ]</i>,
    "<a href="#match" title="Match">Match</a>" : <i>[ <a href="httproute-match.md">Match</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="httproute-action.md">Action</a></i>
<a href="#match" title="Match">Match</a>: <i>
      - <a href="httproute-match.md">Match</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: List of <a href="httproute-action.md">Action</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of <a href="httproute-match.md">Match</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


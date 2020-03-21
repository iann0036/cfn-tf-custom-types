# Terraform::AWS::AppmeshVirtualRouter Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#servicenames" title="ServiceNames">ServiceNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#listener" title="Listener">Listener</a>" : <i>[ <a href="spec-listener.md">Listener</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#servicenames" title="ServiceNames">ServiceNames</a>: <i>
      - String</i>
<a href="#listener" title="Listener">Listener</a>: <i>
      - <a href="spec-listener.md">Listener</a></i>
</pre>

## Properties

#### ServiceNames

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No
_Type_: List of <a href="spec-listener.md">Listener</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# Terraform::AWS::AppmeshVirtualService Provider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#virtualnode" title="VirtualNode">VirtualNode</a>" : <i>[ <a href="provider-virtualnode.md">VirtualNode</a>, ... ]</i>,
    "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>[ <a href="provider-virtualrouter.md">VirtualRouter</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#virtualnode" title="VirtualNode">VirtualNode</a>: <i>
      - <a href="provider-virtualnode.md">VirtualNode</a></i>
<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>
      - <a href="provider-virtualrouter.md">VirtualRouter</a></i>
</pre>

## Properties

#### VirtualNode

_Required_: No

_Type_: List of <a href="provider-virtualnode.md">VirtualNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

_Required_: No

_Type_: List of <a href="provider-virtualrouter.md">VirtualRouter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


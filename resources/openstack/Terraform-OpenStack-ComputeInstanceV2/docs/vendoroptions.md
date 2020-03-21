# Terraform::OpenStack::ComputeInstanceV2 VendorOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ignoreresizeconfirmation" title="IgnoreResizeConfirmation">IgnoreResizeConfirmation</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#ignoreresizeconfirmation" title="IgnoreResizeConfirmation">IgnoreResizeConfirmation</a>: <i>Boolean</i>
</pre>

## Properties

#### IgnoreResizeConfirmation

Boolean to control whether
to ignore manual confirmation of the instance resizing. This can be helpful
to work with some OpenStack clouds which automatically confirm resizing of
instances after some timeout.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# Terraform::OpenStack::ObjectstorageContainerV1 Versioning

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Location

Container in which versions will be stored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Versioning type which can be `versions` or `history` according to [Openstack documentation](https://docs.openstack.org/swift/latest/overview_object_versioning.html).
* `location` - (Required) Container in which versions will be stored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# TF::VSphere::ContentLibrary

The `vsphere_content_library` resource can be used to manage Content Libraries.

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VSphere::ContentLibrary",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#storagebacking" title="StorageBacking">StorageBacking</a>" : <i>[ String, ... ]</i>,
        "<a href="#publication" title="Publication">Publication</a>" : <i>[ <a href="publicationdefinition.md">PublicationDefinition</a>, ... ]</i>,
        "<a href="#subscription" title="Subscription">Subscription</a>" : <i>[ <a href="subscriptiondefinition.md">SubscriptionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VSphere::ContentLibrary
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#storagebacking" title="StorageBacking">StorageBacking</a>: <i>
      - String</i>
    <a href="#publication" title="Publication">Publication</a>: <i>
      - <a href="publicationdefinition.md">PublicationDefinition</a></i>
    <a href="#subscription" title="Subscription">Subscription</a>: <i>
      - <a href="subscriptiondefinition.md">SubscriptionDefinition</a></i>
</pre>

## Properties

#### Description

A description of the Content Library.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Content Library.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageBacking

The [managed object reference ID][docs-about-morefs] on which to store Content Library
items.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publication

_Required_: No

_Type_: List of <a href="publicationdefinition.md">PublicationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subscription

_Required_: No

_Type_: List of <a href="subscriptiondefinition.md">SubscriptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


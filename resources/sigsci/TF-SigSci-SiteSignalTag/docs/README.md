# TF::SigSci::SiteSignalTag

CloudFormation equivalent of sigsci_site_signal_tag

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SigSci::SiteSignalTag",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#siteshortname" title="SiteShortName">SiteShortName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SigSci::SiteSignalTag
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#siteshortname" title="SiteShortName">SiteShortName</a>: <i>String</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteShortName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Configurable

Returns the <code>Configurable</code> value.

#### Id

Returns the <code>Id</code> value.

#### Informational

Returns the <code>Informational</code> value.

#### NeedsResponse

Returns the <code>NeedsResponse</code> value.

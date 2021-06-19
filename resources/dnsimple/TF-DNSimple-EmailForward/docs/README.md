# TF::DNSimple::EmailForward

Provides a DNSimple email forward resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DNSimple::EmailForward",
    "Properties" : {
        "<a href="#aliasname" title="AliasName">AliasName</a>" : <i>String</i>,
        "<a href="#destinationemail" title="DestinationEmail">DestinationEmail</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::DNSimple::EmailForward
Properties:
    <a href="#aliasname" title="AliasName">AliasName</a>: <i>String</i>
    <a href="#destinationemail" title="DestinationEmail">DestinationEmail</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
</pre>

## Properties

#### AliasName

The name part (the part before the @) of the source email address on the domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationEmail

The destination email address on another domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The domain to add the email forwarding rule to.

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

#### Id

Returns the <code>Id</code> value.


# TF::CloudScale::ObjectsUser

Provides a cloudscale.ch Objects User for the S3-compatible object storage.

**Hint**: When using this resource, your Terraform state will contain sensitive data, namely the objects user secret
key. Hence you should treat the Terraform state the same way as you treat the secret key itself. For more
information, see <a href="/docs/state/sensitive-data.html">here</a>.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudScale::ObjectsUser",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudScale::ObjectsUser
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
</pre>

## Properties

#### DisplayName

The new display name of the objects user.

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

#### Href

Returns the <code>Href</code> value.

#### Id

Returns the <code>Id</code> value.

#### Keys

Returns the <code>Keys</code> value.

#### UserId

Returns the <code>UserId</code> value.


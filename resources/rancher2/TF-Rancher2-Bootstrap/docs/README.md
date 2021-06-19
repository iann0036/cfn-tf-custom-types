# TF::Rancher2::Bootstrap

CloudFormation equivalent of rancher2_bootstrap

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::Bootstrap",
    "Properties" : {
        "<a href="#currentpassword" title="CurrentPassword">CurrentPassword</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#telemetry" title="Telemetry">Telemetry</a>" : <i>Boolean</i>,
        "<a href="#tokenttl" title="TokenTtl">TokenTtl</a>" : <i>Double</i>,
        "<a href="#tokenupdate" title="TokenUpdate">TokenUpdate</a>" : <i>Boolean</i>,
        "<a href="#uidefaultlanding" title="UiDefaultLanding">UiDefaultLanding</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::Bootstrap
Properties:
    <a href="#currentpassword" title="CurrentPassword">CurrentPassword</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#telemetry" title="Telemetry">Telemetry</a>: <i>Boolean</i>
    <a href="#tokenttl" title="TokenTtl">TokenTtl</a>: <i>Double</i>
    <a href="#tokenupdate" title="TokenUpdate">TokenUpdate</a>: <i>Boolean</i>
    <a href="#uidefaultlanding" title="UiDefaultLanding">UiDefaultLanding</a>: <i>String</i>
</pre>

## Properties

#### CurrentPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Telemetry

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenUpdate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UiDefaultLanding

_Required_: No

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

#### TempToken

Returns the <code>TempToken</code> value.

#### TempTokenId

Returns the <code>TempTokenId</code> value.

#### Token

Returns the <code>Token</code> value.

#### TokenId

Returns the <code>TokenId</code> value.

#### Url

Returns the <code>Url</code> value.

#### User

Returns the <code>User</code> value.


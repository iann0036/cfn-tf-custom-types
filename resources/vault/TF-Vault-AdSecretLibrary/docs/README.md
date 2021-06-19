# TF::Vault::AdSecretLibrary

CloudFormation equivalent of vault_ad_secret_library

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vault::AdSecretLibrary",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#disablecheckinenforcement" title="DisableCheckInEnforcement">DisableCheckInEnforcement</a>" : <i>Boolean</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#serviceaccountnames" title="ServiceAccountNames">ServiceAccountNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vault::AdSecretLibrary
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#disablecheckinenforcement" title="DisableCheckInEnforcement">DisableCheckInEnforcement</a>: <i>Boolean</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#serviceaccountnames" title="ServiceAccountNames">ServiceAccountNames</a>: <i>
      - String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
</pre>

## Properties

#### Backend

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableCheckInEnforcement

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountNames

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

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


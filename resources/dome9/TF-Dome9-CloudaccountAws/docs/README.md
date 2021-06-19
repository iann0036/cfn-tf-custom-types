# TF::Dome9::CloudaccountAws

CloudFormation equivalent of dome9_cloudaccount_aws

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::CloudaccountAws",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#organizationalunitid" title="OrganizationalUnitId">OrganizationalUnitId</a>" : <i>String</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ <a href="credentialsdefinition.md">CredentialsDefinition</a>, ... ]</i>,
        "<a href="#netsec" title="NetSec">NetSec</a>" : <i>[ <a href="netsecdefinition.md">NetSecDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::CloudaccountAws
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#organizationalunitid" title="OrganizationalUnitId">OrganizationalUnitId</a>: <i>String</i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - <a href="credentialsdefinition.md">CredentialsDefinition</a></i>
    <a href="#netsec" title="NetSec">NetSec</a>: <i>
      - <a href="netsecdefinition.md">NetSecDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationalUnitId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of <a href="credentialsdefinition.md">CredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetSec

_Required_: No

_Type_: List of <a href="netsecdefinition.md">NetSecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllowReadOnly

Returns the <code>AllowReadOnly</code> value.

#### CreationDate

Returns the <code>CreationDate</code> value.

#### ExternalAccountNumber

Returns the <code>ExternalAccountNumber</code> value.

#### FullProtection

Returns the <code>FullProtection</code> value.

#### IamSafe

Returns the <code>IamSafe</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsFetchingSuspended

Returns the <code>IsFetchingSuspended</code> value.

#### Vendor

Returns the <code>Vendor</code> value.


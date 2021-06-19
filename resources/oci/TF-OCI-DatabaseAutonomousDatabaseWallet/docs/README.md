# TF::OCI::DatabaseAutonomousDatabaseWallet

This resource provides the Autonomous Database Wallet resource in Oracle Cloud Infrastructure Database service.

Creates and downloads a wallet for the specified Autonomous Database.

If passing the base64 encoded content to a `local_file` resource, please use the `content_base64` attribute of the `local_file` resource.
See this [example](https://github.com/terraform-providers/terraform-provider-oci/blob/master/examples/database/adb/autonomous_data_warehouse_wallet.tf) for more details.

Recreate the resource to create and download a new wallet.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseAutonomousDatabaseWallet",
    "Properties" : {
        "<a href="#autonomousdatabaseid" title="AutonomousDatabaseId">AutonomousDatabaseId</a>" : <i>String</i>,
        "<a href="#base64encodecontent" title="Base64EncodeContent">Base64EncodeContent</a>" : <i>Boolean</i>,
        "<a href="#generatetype" title="GenerateType">GenerateType</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseAutonomousDatabaseWallet
Properties:
    <a href="#autonomousdatabaseid" title="AutonomousDatabaseId">AutonomousDatabaseId</a>: <i>String</i>
    <a href="#base64encodecontent" title="Base64EncodeContent">Base64EncodeContent</a>: <i>Boolean</i>
    <a href="#generatetype" title="GenerateType">GenerateType</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutonomousDatabaseId

The database [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Base64EncodeContent

Encodes the downloaded zipped wallet in base64. It is recommended to set this to `true` to avoid corrupting the zip file in Terraform state. The default value is `false` to preserve backwards compatibility with Terraform v0.11 configurations.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenerateType

The type of wallet to generate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either 1 numeric character or 1 special character.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Content

Returns the <code>Content</code> value.

#### Id

Returns the <code>Id</code> value.


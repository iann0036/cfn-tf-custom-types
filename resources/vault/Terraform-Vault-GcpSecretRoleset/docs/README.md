# Terraform::Vault::GcpSecretRoleset

Creates a Roleset in the [GCP Secrets Engine](https://www.vaultproject.io/docs/secrets/gcp/index.html) for Vault.

Each Roleset is [tied](https://www.vaultproject.io/docs/secrets/gcp/index.html#service-accounts-are-tied-to-rolesets) to a Service Account, and can have one or more [bindings](https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings) associated with it.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::GcpSecretRoleset",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#roleset" title="Roleset">Roleset</a>" : <i>String</i>,
        "<a href="#secrettype" title="SecretType">SecretType</a>" : <i>String</i>,
        "<a href="#tokenscopes" title="TokenScopes">TokenScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#binding" title="Binding">Binding</a>" : <i>[ <a href="binding.md">Binding</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::GcpSecretRoleset
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#roleset" title="Roleset">Roleset</a>: <i>String</i>
    <a href="#secrettype" title="SecretType">SecretType</a>: <i>String</i>
    <a href="#tokenscopes" title="TokenScopes">TokenScopes</a>: <i>
      - String</i>
    <a href="#binding" title="Binding">Binding</a>: <i>
      - <a href="binding.md">Binding</a></i>
</pre>

## Properties

#### Backend

Path where the GCP Secrets Engine is mounted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

Name of the GCP project that this roleset's service account will belong to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roleset

Name of the Roleset to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretType

Type of secret generated for this role set. Accepted values: `access_token`, `service_account_key`. Defaults to `access_token`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenScopes

List of OAuth scopes to assign to `access_token` secrets generated under this role set (`access_token` role sets only).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Binding

_Required_: No

_Type_: List of <a href="binding.md">Binding</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### ServiceAccountEmail

Returns the <code>ServiceAccountEmail</code> value.


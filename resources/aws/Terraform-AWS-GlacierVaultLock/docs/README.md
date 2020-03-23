# Terraform::AWS::GlacierVaultLock

Manages a Glacier Vault Lock. You can refer to the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html) for a full explanation of the Glacier Vault Lock functionality.

~> **NOTE:** This resource allows you to test Glacier Vault Lock policies by setting the `complete_lock` argument to `false`. When testing policies in this manner, the Glacier Vault Lock automatically expires after 24 hours and Terraform will show this resource as needing recreation after that time. To permanently apply the policy, set the `complete_lock` argument to `true`. When changing `complete_lock` to `true`, it is expected the resource will show as recreating.

!> **WARNING:** Once a Glacier Vault Lock is completed, it is immutable. The deletion of the Glacier Vault Lock is not be possible and attempting to remove it from Terraform will return an error. Set the `ignore_deletion_error` argument to `true` and apply this configuration before attempting to delete this resource via Terraform or use `terraform state rm` to remove this resource from Terraform management.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlacierVaultLock",
    "Properties" : {
        "<a href="#completelock" title="CompleteLock">CompleteLock</a>" : <i>Boolean</i>,
        "<a href="#ignoredeletionerror" title="IgnoreDeletionError">IgnoreDeletionError</a>" : <i>Boolean</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#vaultname" title="VaultName">VaultName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlacierVaultLock
Properties:
    <a href="#completelock" title="CompleteLock">CompleteLock</a>: <i>Boolean</i>
    <a href="#ignoredeletionerror" title="IgnoreDeletionError">IgnoreDeletionError</a>: <i>Boolean</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#vaultname" title="VaultName">VaultName</a>: <i>String</i>
</pre>

## Properties

#### CompleteLock

Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to `false`, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the Terraform resource will show as needing recreation. Changing this from `false` to `true` will show as resource recreation, which is expected. Changing this from `true` to `false` is not possible unless the Glacier Vault is recreated at the same time.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreDeletionError

Allow Terraform to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via Terraform, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with `complete_lock` being set to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultName

The name of the Glacier Vault.

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


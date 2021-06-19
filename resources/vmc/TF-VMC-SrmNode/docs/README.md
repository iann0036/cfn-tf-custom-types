# TF::VMC::SrmNode

Provides a resource to add an instance to SDDC after site recovery has been activated.
~> **Note:** SRM node resource depends on site recovery resource creation. Site recovery must be activated to add SRM node instance. For details on how to activate site recovery refer to the site recovery resource [vmc_site_recovery](https://www.terraform.io/docs/providers/vmc/r/site_recovery.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VMC::SrmNode",
    "Properties" : {
        "<a href="#sddcid" title="SddcId">SddcId</a>" : <i>String</i>,
        "<a href="#srmnodeextensionkeysuffix" title="SrmNodeExtensionKeySuffix">SrmNodeExtensionKeySuffix</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VMC::SrmNode
Properties:
    <a href="#sddcid" title="SddcId">SddcId</a>: <i>String</i>
    <a href="#srmnodeextensionkeysuffix" title="SrmNodeExtensionKeySuffix">SrmNodeExtensionKeySuffix</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### SddcId

SDDC identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrmNodeExtensionKeySuffix

Custom extension key suffix for SRM. If not specified, default extension key will be used.
The custom extension suffix must contain 13 characters or less, be composed of letters, numbers, ., - characters.
The extension suffix must begin and end with a letter or number. The suffix is appended to com.vmware.vcDr- to form the full extension key.

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

#### Id

Returns the <code>Id</code> value.

#### SrmInstance

Returns the <code>SrmInstance</code> value.


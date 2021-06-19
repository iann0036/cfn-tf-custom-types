# TF::VMC::SiteRecovery

Provides a resource to activate and deactivate site recovery for SDDC.

~> **Note:** Site recovery resource implicitly depends on SDDC resource creation. SDDC must be provisioned before a site recovery can be activated. 
A 10 minute delay must be added to SDDC resource before site recovery can be activated.
This delay is added using using the local-exec provisioner. For details on how to provision SDDC refer to [vmc_sddc](https://www.terraform.io/docs/providers/vmc/r/sddc.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VMC::SiteRecovery",
    "Properties" : {
        "<a href="#sddcid" title="SddcId">SddcId</a>" : <i>String</i>,
        "<a href="#srmextensionkeysuffix" title="SrmExtensionKeySuffix">SrmExtensionKeySuffix</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VMC::SiteRecovery
Properties:
    <a href="#sddcid" title="SddcId">SddcId</a>: <i>String</i>
    <a href="#srmextensionkeysuffix" title="SrmExtensionKeySuffix">SrmExtensionKeySuffix</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### SddcId

SDDC identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrmExtensionKeySuffix

_Required_: No

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

#### SiteRecoveryState

Returns the <code>SiteRecoveryState</code> value.

#### SrmNode

Returns the <code>SrmNode</code> value.

#### UserId

Returns the <code>UserId</code> value.

#### UserName

Returns the <code>UserName</code> value.

#### VrNode

Returns the <code>VrNode</code> value.


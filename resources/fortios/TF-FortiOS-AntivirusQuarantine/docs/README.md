# TF::FortiOS::AntivirusQuarantine

Configure quarantine options.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::AntivirusQuarantine",
    "Properties" : {
        "<a href="#agelimit" title="Agelimit">Agelimit</a>" : <i>Double</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#dropblocked" title="DropBlocked">DropBlocked</a>" : <i>String</i>,
        "<a href="#dropheuristic" title="DropHeuristic">DropHeuristic</a>" : <i>String</i>,
        "<a href="#dropinfected" title="DropInfected">DropInfected</a>" : <i>String</i>,
        "<a href="#lowspace" title="Lowspace">Lowspace</a>" : <i>String</i>,
        "<a href="#maxfilesize" title="Maxfilesize">Maxfilesize</a>" : <i>Double</i>,
        "<a href="#quarantinequota" title="QuarantineQuota">QuarantineQuota</a>" : <i>Double</i>,
        "<a href="#storeblocked" title="StoreBlocked">StoreBlocked</a>" : <i>String</i>,
        "<a href="#storeheuristic" title="StoreHeuristic">StoreHeuristic</a>" : <i>String</i>,
        "<a href="#storeinfected" title="StoreInfected">StoreInfected</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::AntivirusQuarantine
Properties:
    <a href="#agelimit" title="Agelimit">Agelimit</a>: <i>Double</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#dropblocked" title="DropBlocked">DropBlocked</a>: <i>String</i>
    <a href="#dropheuristic" title="DropHeuristic">DropHeuristic</a>: <i>String</i>
    <a href="#dropinfected" title="DropInfected">DropInfected</a>: <i>String</i>
    <a href="#lowspace" title="Lowspace">Lowspace</a>: <i>String</i>
    <a href="#maxfilesize" title="Maxfilesize">Maxfilesize</a>: <i>Double</i>
    <a href="#quarantinequota" title="QuarantineQuota">QuarantineQuota</a>: <i>Double</i>
    <a href="#storeblocked" title="StoreBlocked">StoreBlocked</a>: <i>String</i>
    <a href="#storeheuristic" title="StoreHeuristic">StoreHeuristic</a>: <i>String</i>
    <a href="#storeinfected" title="StoreInfected">StoreInfected</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Agelimit

Age limit for quarantined files (0 - 479 hours, 0 means forever).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

Choose whether to quarantine files to the FortiGate disk or to FortiAnalyzer or to delete them instead of quarantining them. Valid values: `NULL`, `disk`, `FortiAnalyzer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropBlocked

Do not quarantine dropped files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropHeuristic

Do not quarantine files detected by heuristics found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropInfected

Do not quarantine infected files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lowspace

Select the method for handling additional files when running low on disk space. Valid values: `drop-new`, `ovrw-old`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maxfilesize

Maximum file size to quarantine (0 - 500 Mbytes, 0 means unlimited).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineQuota

The amount of disk space to reserve for quarantining files (0 - 4294967295 Mbytes, depends on disk space).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoreBlocked

Quarantine blocked files found in sessions using the selected protocols.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoreHeuristic

Quarantine files detected by heuristics found in sessions using the selected protocols.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoreInfected

Quarantine infected files found in sessions using the selected protocols.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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


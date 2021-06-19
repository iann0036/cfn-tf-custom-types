# TF::ECL::SecurityNetworkBasedDeviceHaV2

Manages a V2 Network Based Device(Single) resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::SecurityNetworkBasedDeviceHaV2",
    "Properties" : {
        "<a href="#host1azgroup" title="Host1AzGroup">Host1AzGroup</a>" : <i>String</i>,
        "<a href="#host2azgroup" title="Host2AzGroup">Host2AzGroup</a>" : <i>String</i>,
        "<a href="#licensekind" title="LicenseKind">LicenseKind</a>" : <i>String</i>,
        "<a href="#locale" title="Locale">Locale</a>" : <i>String</i>,
        "<a href="#operatingmode" title="OperatingMode">OperatingMode</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#halink1" title="HaLink1">HaLink1</a>" : <i>[ <a href="halink1definition.md">HaLink1Definition</a>, ... ]</i>,
        "<a href="#halink2" title="HaLink2">HaLink2</a>" : <i>[ <a href="halink2definition.md">HaLink2Definition</a>, ... ]</i>,
        "<a href="#port" title="Port">Port</a>" : <i>[ <a href="portdefinition.md">PortDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::SecurityNetworkBasedDeviceHaV2
Properties:
    <a href="#host1azgroup" title="Host1AzGroup">Host1AzGroup</a>: <i>String</i>
    <a href="#host2azgroup" title="Host2AzGroup">Host2AzGroup</a>: <i>String</i>
    <a href="#licensekind" title="LicenseKind">LicenseKind</a>: <i>String</i>
    <a href="#locale" title="Locale">Locale</a>: <i>String</i>
    <a href="#operatingmode" title="OperatingMode">OperatingMode</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#halink1" title="HaLink1">HaLink1</a>: <i>
      - <a href="halink1definition.md">HaLink1Definition</a></i>
    <a href="#halink2" title="HaLink2">HaLink2</a>: <i>
      - <a href="halink2definition.md">HaLink2Definition</a></i>
    <a href="#port" title="Port">Port</a>: <i>
      - <a href="portdefinition.md">PortDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Host1AzGroup

Set availability zone for HA Host 1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host2AzGroup

Set availability zone for HA Host 2.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseKind

Set "02" or "08" as FW/UTM plan.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locale

Messages are displayed in Japanese or English depending on this value.
ja: Japanese, en: English. Default value is "en".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingMode

Set "FW" or "UTM" to this value.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Tenant ID of the owner (UUID).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaLink1

_Required_: No

_Type_: List of <a href="halink1definition.md">HaLink1Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaLink2

_Required_: No

_Type_: List of <a href="halink2definition.md">HaLink2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="portdefinition.md">PortDefinition</a>

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


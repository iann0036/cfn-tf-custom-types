# TF::Thunder::SnmpServerEnableTrapsRoutingIsis

`thunder_snmp_server_enable_traps_routing_isis` Provides details about thunder snmp server enable traps routing isis

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerEnableTrapsRoutingIsis",
    "Properties" : {
        "<a href="#isisadjacencychange" title="IsisAdjacencyChange">IsisAdjacencyChange</a>" : <i>Double</i>,
        "<a href="#isisareamismatch" title="IsisAreaMismatch">IsisAreaMismatch</a>" : <i>Double</i>,
        "<a href="#isisattempttoexceedmaxsequence" title="IsisAttemptToExceedMaxSequence">IsisAttemptToExceedMaxSequence</a>" : <i>Double</i>,
        "<a href="#isisauthenticationfailure" title="IsisAuthenticationFailure">IsisAuthenticationFailure</a>" : <i>Double</i>,
        "<a href="#isisauthenticationtypefailure" title="IsisAuthenticationTypeFailure">IsisAuthenticationTypeFailure</a>" : <i>Double</i>,
        "<a href="#isiscorruptedlspdetected" title="IsisCorruptedLspDetected">IsisCorruptedLspDetected</a>" : <i>Double</i>,
        "<a href="#isisdatabaseoverload" title="IsisDatabaseOverload">IsisDatabaseOverload</a>" : <i>Double</i>,
        "<a href="#isisidlenmismatch" title="IsisIdLenMismatch">IsisIdLenMismatch</a>" : <i>Double</i>,
        "<a href="#isislsptoolargetopropagate" title="IsisLspTooLargeToPropagate">IsisLspTooLargeToPropagate</a>" : <i>Double</i>,
        "<a href="#isismanualaddressdrops" title="IsisManualAddressDrops">IsisManualAddressDrops</a>" : <i>Double</i>,
        "<a href="#isismaxareaaddressesmismatch" title="IsisMaxAreaAddressesMismatch">IsisMaxAreaAddressesMismatch</a>" : <i>Double</i>,
        "<a href="#isisoriginatinglspbuffersizemismatch" title="IsisOriginatingLspBufferSizeMismatch">IsisOriginatingLspBufferSizeMismatch</a>" : <i>Double</i>,
        "<a href="#isisownlsppurge" title="IsisOwnLspPurge">IsisOwnLspPurge</a>" : <i>Double</i>,
        "<a href="#isisprotocolssupportedmismatch" title="IsisProtocolsSupportedMismatch">IsisProtocolsSupportedMismatch</a>" : <i>Double</i>,
        "<a href="#isisrejectedadjacency" title="IsisRejectedAdjacency">IsisRejectedAdjacency</a>" : <i>Double</i>,
        "<a href="#isissequencenumberskip" title="IsisSequenceNumberSkip">IsisSequenceNumberSkip</a>" : <i>Double</i>,
        "<a href="#isisversionskew" title="IsisVersionSkew">IsisVersionSkew</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerEnableTrapsRoutingIsis
Properties:
    <a href="#isisadjacencychange" title="IsisAdjacencyChange">IsisAdjacencyChange</a>: <i>Double</i>
    <a href="#isisareamismatch" title="IsisAreaMismatch">IsisAreaMismatch</a>: <i>Double</i>
    <a href="#isisattempttoexceedmaxsequence" title="IsisAttemptToExceedMaxSequence">IsisAttemptToExceedMaxSequence</a>: <i>Double</i>
    <a href="#isisauthenticationfailure" title="IsisAuthenticationFailure">IsisAuthenticationFailure</a>: <i>Double</i>
    <a href="#isisauthenticationtypefailure" title="IsisAuthenticationTypeFailure">IsisAuthenticationTypeFailure</a>: <i>Double</i>
    <a href="#isiscorruptedlspdetected" title="IsisCorruptedLspDetected">IsisCorruptedLspDetected</a>: <i>Double</i>
    <a href="#isisdatabaseoverload" title="IsisDatabaseOverload">IsisDatabaseOverload</a>: <i>Double</i>
    <a href="#isisidlenmismatch" title="IsisIdLenMismatch">IsisIdLenMismatch</a>: <i>Double</i>
    <a href="#isislsptoolargetopropagate" title="IsisLspTooLargeToPropagate">IsisLspTooLargeToPropagate</a>: <i>Double</i>
    <a href="#isismanualaddressdrops" title="IsisManualAddressDrops">IsisManualAddressDrops</a>: <i>Double</i>
    <a href="#isismaxareaaddressesmismatch" title="IsisMaxAreaAddressesMismatch">IsisMaxAreaAddressesMismatch</a>: <i>Double</i>
    <a href="#isisoriginatinglspbuffersizemismatch" title="IsisOriginatingLspBufferSizeMismatch">IsisOriginatingLspBufferSizeMismatch</a>: <i>Double</i>
    <a href="#isisownlsppurge" title="IsisOwnLspPurge">IsisOwnLspPurge</a>: <i>Double</i>
    <a href="#isisprotocolssupportedmismatch" title="IsisProtocolsSupportedMismatch">IsisProtocolsSupportedMismatch</a>: <i>Double</i>
    <a href="#isisrejectedadjacency" title="IsisRejectedAdjacency">IsisRejectedAdjacency</a>: <i>Double</i>
    <a href="#isissequencenumberskip" title="IsisSequenceNumberSkip">IsisSequenceNumberSkip</a>: <i>Double</i>
    <a href="#isisversionskew" title="IsisVersionSkew">IsisVersionSkew</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### IsisAdjacencyChange

Enable isisAdjacencyChange traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisAreaMismatch

Enable isisAreaMismatch traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisAttemptToExceedMaxSequence

Enable isisAttemptToExceedMaxSequence traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisAuthenticationFailure

Enable isisAuthenticationFailure traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisAuthenticationTypeFailure

Enable isisAuthenticationTypeFailure traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisCorruptedLspDetected

Enable isisCorruptedLSPDetected traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisDatabaseOverload

Enable isisDatabaseOverload traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisIdLenMismatch

Enable isisIDLenMismatch traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisLspTooLargeToPropagate

Enable isisLSPTooLargeToPropagate traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisManualAddressDrops

Enable isisManualAddressDrops traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisMaxAreaAddressesMismatch

Enable isisMaxAreaAddressesMismatch traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisOriginatingLspBufferSizeMismatch

Enable isisOriginatingLSPBufferSizeMismatch traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisOwnLspPurge

Enable isisOwnLSPPurge traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisProtocolsSupportedMismatch

Enable isisProtocolsSupportedMismatch traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisRejectedAdjacency

Enable isisRejectedAdjacency traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisSequenceNumberSkip

Enable isisSequenceNumberSkip traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisVersionSkew

Enable isisVersionSkew traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

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


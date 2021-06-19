# TF::Aviatrix::VgwConn

The **aviatrix_vgw_conn** resource manages the connection between the Aviatrix transit gateway and AWS VGW for purposes of Transit Network.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::VgwConn",
    "Properties" : {
        "<a href="#bgplocalasnum" title="BgpLocalAsNum">BgpLocalAsNum</a>" : <i>String</i>,
        "<a href="#bgpvgwaccount" title="BgpVgwAccount">BgpVgwAccount</a>" : <i>String</i>,
        "<a href="#bgpvgwid" title="BgpVgwId">BgpVgwId</a>" : <i>String</i>,
        "<a href="#bgpvgwregion" title="BgpVgwRegion">BgpVgwRegion</a>" : <i>String</i>,
        "<a href="#connname" title="ConnName">ConnName</a>" : <i>String</i>,
        "<a href="#enableeventtriggeredha" title="EnableEventTriggeredHa">EnableEventTriggeredHa</a>" : <i>Boolean</i>,
        "<a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>" : <i>Boolean</i>,
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#manualbgpadvertisedcidrs" title="ManualBgpAdvertisedCidrs">ManualBgpAdvertisedCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::VgwConn
Properties:
    <a href="#bgplocalasnum" title="BgpLocalAsNum">BgpLocalAsNum</a>: <i>String</i>
    <a href="#bgpvgwaccount" title="BgpVgwAccount">BgpVgwAccount</a>: <i>String</i>
    <a href="#bgpvgwid" title="BgpVgwId">BgpVgwId</a>: <i>String</i>
    <a href="#bgpvgwregion" title="BgpVgwRegion">BgpVgwRegion</a>: <i>String</i>
    <a href="#connname" title="ConnName">ConnName</a>: <i>String</i>
    <a href="#enableeventtriggeredha" title="EnableEventTriggeredHa">EnableEventTriggeredHa</a>: <i>Boolean</i>
    <a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>: <i>Boolean</i>
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#manualbgpadvertisedcidrs" title="ManualBgpAdvertisedCidrs">ManualBgpAdvertisedCidrs</a>: <i>
      - String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### BgpLocalAsNum

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpVgwAccount

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpVgwId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpVgwRegion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEventTriggeredHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLearnedCidrsApproval

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualBgpAdvertisedCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

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


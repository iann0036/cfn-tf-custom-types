# TF::Alicloud::CenRouteMap

This topic provides an overview of the route map function of Cloud Enterprise Networks (CENs).
You can use the route map function to filter routes and modify route attributes.
By doing so, you can manage the communication between networks attached to a CEN. 

For information about CEN Route Map and how to use it, see [Manage CEN Route Map](https://www.alibabacloud.com/help/doc-detail/124157.htm).

-> **NOTE:** Available in 1.82.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CenRouteMap",
    "Properties" : {
        "<a href="#aspathmatchmode" title="AsPathMatchMode">AsPathMatchMode</a>" : <i>String</i>,
        "<a href="#cenid" title="CenId">CenId</a>" : <i>String</i>,
        "<a href="#cenregionid" title="CenRegionId">CenRegionId</a>" : <i>String</i>,
        "<a href="#cidrmatchmode" title="CidrMatchMode">CidrMatchMode</a>" : <i>String</i>,
        "<a href="#communitymatchmode" title="CommunityMatchMode">CommunityMatchMode</a>" : <i>String</i>,
        "<a href="#communityoperatemode" title="CommunityOperateMode">CommunityOperateMode</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationchildinstancetypes" title="DestinationChildInstanceTypes">DestinationChildInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationcidrblocks" title="DestinationCidrBlocks">DestinationCidrBlocks</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationinstanceids" title="DestinationInstanceIds">DestinationInstanceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationinstanceidsreversematch" title="DestinationInstanceIdsReverseMatch">DestinationInstanceIdsReverseMatch</a>" : <i>Boolean</i>,
        "<a href="#destinationroutetableids" title="DestinationRouteTableIds">DestinationRouteTableIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#mapresult" title="MapResult">MapResult</a>" : <i>String</i>,
        "<a href="#matchasns" title="MatchAsns">MatchAsns</a>" : <i>[ String, ... ]</i>,
        "<a href="#matchcommunityset" title="MatchCommunitySet">MatchCommunitySet</a>" : <i>[ String, ... ]</i>,
        "<a href="#nextpriority" title="NextPriority">NextPriority</a>" : <i>Double</i>,
        "<a href="#operatecommunityset" title="OperateCommunitySet">OperateCommunitySet</a>" : <i>[ String, ... ]</i>,
        "<a href="#preference" title="Preference">Preference</a>" : <i>Double</i>,
        "<a href="#prependaspath" title="PrependAsPath">PrependAsPath</a>" : <i>[ String, ... ]</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#routetypes" title="RouteTypes">RouteTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcechildinstancetypes" title="SourceChildInstanceTypes">SourceChildInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourceinstanceids" title="SourceInstanceIds">SourceInstanceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourceinstanceidsreversematch" title="SourceInstanceIdsReverseMatch">SourceInstanceIdsReverseMatch</a>" : <i>Boolean</i>,
        "<a href="#sourceregionids" title="SourceRegionIds">SourceRegionIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourceroutetableids" title="SourceRouteTableIds">SourceRouteTableIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#transmitdirection" title="TransmitDirection">TransmitDirection</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CenRouteMap
Properties:
    <a href="#aspathmatchmode" title="AsPathMatchMode">AsPathMatchMode</a>: <i>String</i>
    <a href="#cenid" title="CenId">CenId</a>: <i>String</i>
    <a href="#cenregionid" title="CenRegionId">CenRegionId</a>: <i>String</i>
    <a href="#cidrmatchmode" title="CidrMatchMode">CidrMatchMode</a>: <i>String</i>
    <a href="#communitymatchmode" title="CommunityMatchMode">CommunityMatchMode</a>: <i>String</i>
    <a href="#communityoperatemode" title="CommunityOperateMode">CommunityOperateMode</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationchildinstancetypes" title="DestinationChildInstanceTypes">DestinationChildInstanceTypes</a>: <i>
      - String</i>
    <a href="#destinationcidrblocks" title="DestinationCidrBlocks">DestinationCidrBlocks</a>: <i>
      - String</i>
    <a href="#destinationinstanceids" title="DestinationInstanceIds">DestinationInstanceIds</a>: <i>
      - String</i>
    <a href="#destinationinstanceidsreversematch" title="DestinationInstanceIdsReverseMatch">DestinationInstanceIdsReverseMatch</a>: <i>Boolean</i>
    <a href="#destinationroutetableids" title="DestinationRouteTableIds">DestinationRouteTableIds</a>: <i>
      - String</i>
    <a href="#mapresult" title="MapResult">MapResult</a>: <i>String</i>
    <a href="#matchasns" title="MatchAsns">MatchAsns</a>: <i>
      - String</i>
    <a href="#matchcommunityset" title="MatchCommunitySet">MatchCommunitySet</a>: <i>
      - String</i>
    <a href="#nextpriority" title="NextPriority">NextPriority</a>: <i>Double</i>
    <a href="#operatecommunityset" title="OperateCommunitySet">OperateCommunitySet</a>: <i>
      - String</i>
    <a href="#preference" title="Preference">Preference</a>: <i>Double</i>
    <a href="#prependaspath" title="PrependAsPath">PrependAsPath</a>: <i>
      - String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#routetypes" title="RouteTypes">RouteTypes</a>: <i>
      - String</i>
    <a href="#sourcechildinstancetypes" title="SourceChildInstanceTypes">SourceChildInstanceTypes</a>: <i>
      - String</i>
    <a href="#sourceinstanceids" title="SourceInstanceIds">SourceInstanceIds</a>: <i>
      - String</i>
    <a href="#sourceinstanceidsreversematch" title="SourceInstanceIdsReverseMatch">SourceInstanceIdsReverseMatch</a>: <i>Boolean</i>
    <a href="#sourceregionids" title="SourceRegionIds">SourceRegionIds</a>: <i>
      - String</i>
    <a href="#sourceroutetableids" title="SourceRouteTableIds">SourceRouteTableIds</a>: <i>
      - String</i>
    <a href="#transmitdirection" title="TransmitDirection">TransmitDirection</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AsPathMatchMode

A match statement. It indicates the mode in which the AS path attribute is matched. Valid values: ["Include", "Complete"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CenId

The ID of the CEN instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CenRegionId

The ID of the region to which the CEN instance belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrMatchMode

A match statement. It indicates the mode in which the prefix attribute is matched. Valid values: ["Include", "Complete"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityMatchMode

A match statement. It indicates the mode in which the community attribute is matched. Valid values: ["Include", "Complete"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityOperateMode

An action statement. It indicates the mode in which the community attribute is operated. Valid values: ["Additive", "Replace"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the route map.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationChildInstanceTypes

A match statement that indicates the list of destination instance types. Valid values: ["VPC", "VBR", "CCN"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationCidrBlocks

A match statement that indicates the prefix list. The prefix is in the CIDR format. You can enter a maximum of 32 CIDR blocks.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationInstanceIds

A match statement that indicates the list of IDs of the destination instances.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationInstanceIdsReverseMatch

Indicates whether to enable the reverse match method for the DestinationInstanceIds match condition. Valid values: ["false", "true"]. Default to "false".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationRouteTableIds

A match statement that indicates the list of IDs of the destination route tables. You can enter a maximum of 32 route table IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MapResult

The action that is performed to a route if the route matches all the match conditions. Valid values: ["Permit", "Deny"].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAsns

A match statement that indicates the AS path list. The AS path is a well-known mandatory attribute, which describes the numbers of the ASs that a BGP route passes through during transmission.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCommunitySet

A match statement that indicates the community set. The format of each community is nn:nn, which ranges from 1 to 65535. You can enter a maximum of 32 communities. Communities must comply with RFC 1997. Large communities (RFC 8092) are not supported.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextPriority

The priority of the next route map that is associated with the current route map. Value range: 1 to 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperateCommunitySet

An action statement that operates the community attribute. The format of each community is nn:nn, which ranges from 1 to 65535. You can enter a maximum of 32 communities. Communities must comply with RFC 1997. Large communities (RFC 8092) are not supported.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preference

An action statement that modifies the priority of the route. Value range: 1 to 100. The default priority of a route is 50. A lower value indicates a higher preference.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrependAsPath

An action statement that indicates an AS path is prepended when the regional gateway receives or advertises a route.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority of the route map. Value range: 1 to 100. A lower value indicates a higher priority.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTypes

A match statement that indicates the list of route types. Valid values: ["System", "Custom", "BGP"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceChildInstanceTypes

A match statement that indicates the list of source instance types. Valid values: ["VPC", "VBR", "CCN"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceInstanceIds

A match statement that indicates the list of IDs of the source instances.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceInstanceIdsReverseMatch

Indicates whether to enable the reverse match method for the SourceInstanceIds match condition. Valid values: ["false", "true"]. Default to "false".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRegionIds

A match statement that indicates the list of IDs of the source regions. You can enter a maximum of 32 region IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRouteTableIds

A match statement that indicates the list of IDs of the source route tables. You can enter a maximum of 32 route table IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransmitDirection

The direction in which the route map is applied. Valid values: ["RegionIn", "RegionOut"].

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

#### RouteMapId

Returns the <code>RouteMapId</code> value.

#### Status

Returns the <code>Status</code> value.


# TF::ACI::BgpPeerConnectivityProfile

Manages ACI BGP Peer Connectivity Profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::BgpPeerConnectivityProfile",
    "Properties" : {
        "<a href="#addr" title="Addr">Addr</a>" : <i>String</i>,
        "<a href="#addrtctrl" title="AddrTCtrl">AddrTCtrl</a>" : <i>String</i>,
        "<a href="#allowedselfascnt" title="AllowedSelfAsCnt">AllowedSelfAsCnt</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>String</i>,
        "<a href="#ctrl" title="Ctrl">Ctrl</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#localasn" title="LocalAsn">LocalAsn</a>" : <i>String</i>,
        "<a href="#localasnpropagate" title="LocalAsnPropagate">LocalAsnPropagate</a>" : <i>String</i>,
        "<a href="#logicalnodeprofiledn" title="LogicalNodeProfileDn">LogicalNodeProfileDn</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#peerctrl" title="PeerCtrl">PeerCtrl</a>" : <i>String</i>,
        "<a href="#privateasctrl" title="PrivateASctrl">PrivateASctrl</a>" : <i>String</i>,
        "<a href="#relationbgprspeerpfxpol" title="RelationBgpRsPeerPfxPol">RelationBgpRsPeerPfxPol</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::BgpPeerConnectivityProfile
Properties:
    <a href="#addr" title="Addr">Addr</a>: <i>String</i>
    <a href="#addrtctrl" title="AddrTCtrl">AddrTCtrl</a>: <i>String</i>
    <a href="#allowedselfascnt" title="AllowedSelfAsCnt">AllowedSelfAsCnt</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>String</i>
    <a href="#ctrl" title="Ctrl">Ctrl</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#localasn" title="LocalAsn">LocalAsn</a>: <i>String</i>
    <a href="#localasnpropagate" title="LocalAsnPropagate">LocalAsnPropagate</a>: <i>String</i>
    <a href="#logicalnodeprofiledn" title="LogicalNodeProfileDn">LogicalNodeProfileDn</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#peerctrl" title="PeerCtrl">PeerCtrl</a>: <i>String</i>
    <a href="#privateasctrl" title="PrivateASctrl">PrivateASctrl</a>: <i>String</i>
    <a href="#relationbgprspeerpfxpol" title="RelationBgpRsPeerPfxPol">RelationBgpRsPeerPfxPol</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>String</i>
</pre>

## Properties

#### Addr

The peer IP address.
- `addr_t_ctrl` - (Optional) Ucast/Mcast Addr Type AF Control. (Multiple Comma-Delimited values are allowed. E.g., "af-mcast,af-ucast"). Apply "" to clear all the values.
Allowed values: "af-mcast", "af-ucast". Default value: "af-ucast".
- `allowed_self_as_cnt` - (Optional) The number of occurrences of a local Autonomous System Number (ASN). Default value: "3".
- `description` - (Optional) Description for object bgp peer connectivity profile.
- `annotation` - (Optional) Annotation for object bgp peer connectivity profile.
- `ctrl` - (Optional)
The peer controls specify which Border Gateway Protocol (BGP) attributes are sent to a peer. (Multiple Comma-Delimited values are allowed. E.g., "allow-self-as,as-override"). Apply "" to clear all the values.
Allowed values: "allow-self-as", "as-override", "dis-peer-as-check", "nh-self", "send-com", "send-ext-com". Default value: "".
- `name_alias` - (Optional) Name alias for object bgp peer connectivity profile.
- `password` - (Optional, Sensitive) Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddrTCtrl

Ucast/Mcast Addr Type AF Control. (Multiple Comma-Delimited values are allowed. E.g., "af-mcast,af-ucast"). Apply "" to clear all the values.
Allowed values: "af-mcast", "af-ucast". Default value: "af-ucast".
- `allowed_self_as_cnt` - (Optional) The number of occurrences of a local Autonomous System Number (ASN). Default value: "3".
- `description` - (Optional) Description for object bgp peer connectivity profile.
- `annotation` - (Optional) Annotation for object bgp peer connectivity profile.
- `ctrl` - (Optional)
The peer controls specify which Border Gateway Protocol (BGP) attributes are sent to a peer. (Multiple Comma-Delimited values are allowed. E.g., "allow-self-as,as-override"). Apply "" to clear all the values.
Allowed values: "allow-self-as", "as-override", "dis-peer-as-check", "nh-self", "send-com", "send-ext-com". Default value: "".
- `name_alias` - (Optional) Name alias for object bgp peer connectivity profile.
- `password` - (Optional, Sensitive) Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedSelfAsCnt

The number of occurrences of a local Autonomous System Number (ASN). Default value: "3".
- `description` - (Optional) Description for object bgp peer connectivity profile.
- `annotation` - (Optional) Annotation for object bgp peer connectivity profile.
- `ctrl` - (Optional)
The peer controls specify which Border Gateway Protocol (BGP) attributes are sent to a peer. (Multiple Comma-Delimited values are allowed. E.g., "allow-self-as,as-override"). Apply "" to clear all the values.
Allowed values: "allow-self-as", "as-override", "dis-peer-as-check", "nh-self", "send-com", "send-ext-com". Default value: "".
- `name_alias` - (Optional) Name alias for object bgp peer connectivity profile.
- `password` - (Optional, Sensitive) Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

Annotation for object bgp peer connectivity profile.
- `ctrl` - (Optional)
The peer controls specify which Border Gateway Protocol (BGP) attributes are sent to a peer. (Multiple Comma-Delimited values are allowed. E.g., "allow-self-as,as-override"). Apply "" to clear all the values.
Allowed values: "allow-self-as", "as-override", "dis-peer-as-check", "nh-self", "send-com", "send-ext-com". Default value: "".
- `name_alias` - (Optional) Name alias for object bgp peer connectivity profile.
- `password` - (Optional, Sensitive) Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsNumber

A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ctrl

The peer controls specify which Border Gateway Protocol (BGP) attributes are sent to a peer. (Multiple Comma-Delimited values are allowed. E.g., "allow-self-as,as-override"). Apply "" to clear all the values.
Allowed values: "allow-self-as", "as-override", "dis-peer-as-check", "nh-self", "send-com", "send-ext-com". Default value: "".
- `name_alias` - (Optional) Name alias for object bgp peer connectivity profile.
- `password` - (Optional, Sensitive) Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object bgp peer connectivity profile.
- `annotation` - (Optional) Annotation for object bgp peer connectivity profile.
- `ctrl` - (Optional)
The peer controls specify which Border Gateway Protocol (BGP) attributes are sent to a peer. (Multiple Comma-Delimited values are allowed. E.g., "allow-self-as,as-override"). Apply "" to clear all the values.
Allowed values: "allow-self-as", "as-override", "dis-peer-as-check", "nh-self", "send-com", "send-ext-com". Default value: "".
- `name_alias` - (Optional) Name alias for object bgp peer connectivity profile.
- `password` - (Optional, Sensitive) Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAsn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAsnPropagate

The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalNodeProfileDn

Distinguished name of parent logical node profile object.
- `addr` - (Required) The peer IP address.
- `addr_t_ctrl` - (Optional) Ucast/Mcast Addr Type AF Control. (Multiple Comma-Delimited values are allowed. E.g., "af-mcast,af-ucast"). Apply "" to clear all the values.
Allowed values: "af-mcast", "af-ucast". Default value: "af-ucast".
- `allowed_self_as_cnt` - (Optional) The number of occurrences of a local Autonomous System Number (ASN). Default value: "3".
- `description` - (Optional) Description for object bgp peer connectivity profile.
- `annotation` - (Optional) Annotation for object bgp peer connectivity profile.
- `ctrl` - (Optional)
The peer controls specify which Border Gateway Protocol (BGP) attributes are sent to a peer. (Multiple Comma-Delimited values are allowed. E.g., "allow-self-as,as-override"). Apply "" to clear all the values.
Allowed values: "allow-self-as", "as-override", "dis-peer-as-check", "nh-self", "send-com", "send-ext-com". Default value: "".
- `name_alias` - (Optional) Name alias for object bgp peer connectivity profile.
- `password` - (Optional, Sensitive) Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object bgp peer connectivity profile.
- `password` - (Optional, Sensitive) Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Peer password. If `password` is set, the peer password will reset when terraform configuration is applied.
- `peer_ctrl` - (Optional) The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerCtrl

The peer controls. (Multiple Comma-Delimited values are allowed. E.g., "bfd,dis-conn-check"). Apply "" to clear all the values.
Allowed values: "bfd", "dis-conn-check". Default value: "".
- `private_a_sctrl` - (Optional) Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateASctrl

Remove private AS. (Multiple Comma-Delimited values are allowed. E.g., "remove-all,remove-exclusive"). Apply "" to clear all the values.
Allowed values: "remove-all", "remove-exclusive", "replace-as". Default value: "".
- `ttl` - (Optional) Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationBgpRsPeerPfxPol

Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Specifies time to live (TTL). Default value: "1".
- `weight` - (Optional) The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object. Default value: "0".
- `as_number` - (Optional) A number that uniquely identifies an autonomous system.
- `local_asn ` - (Optional) The local autonomous system number (ASN).
- `local_asn_propagate` - (Optional) The local Autonomous System Number (ASN) configuration.
Allowed values: "dual-as", "no-prepend", "none", "replace-as". Default value: "none".
- `relation_bgp_rs_peer_pfx_pol` - (Optional) Relation to class bgpPeerPfxPol. Cardinality - N_TO_ONE. Type - String.

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


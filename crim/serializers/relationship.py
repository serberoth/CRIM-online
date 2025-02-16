from crim.models.definition import CRIMDefinition
from crim.models.person import CRIMPerson
from crim.models.piece import CRIMPiece
from crim.models.relationship import CRIMRelationship, CJRelationship
from crim.models.role import CRIMRole, CRIMRoleType
from crim.models.observation import CRIMObservation, CJObservation
from crim.serializers.observation import CRIMObservationBriefSerializer
from crim.serializers.observation import CJObservationBriefSerializer
from rest_framework import serializers


class CRIMDefinitionRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimdefinition-detail-data', lookup_field='id')

    class Meta:
        model = CRIMDefinition
        fields = (
            'url',
            'id',
            'relationship_definition',
        )


class CRIMDefinitionObservationRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimdefinition-detail-data', lookup_field='id')

    class Meta:
        model = CRIMDefinition
        fields = (
            'url',
            'id',
            'observation_definition',
        )


class CRIMPersonRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimperson-detail-data', lookup_field='person_id')

    class Meta:
        model = CRIMPerson
        fields = (
            'url',
            'name',
            'id',
        )


class CRIMRoleTypeRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimroletype-detail-data', lookup_field='role_type_id')

    class Meta:
        model = CRIMRoleType
        fields = (
            'url',
            'role_type_id',
            'name',
        )


class CRIMRoleRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimrole-detail-data', lookup_field='id')
    person = CRIMPersonRelationshipSerializer(read_only=True)
    role_type = CRIMRoleTypeRelationshipSerializer(read_only=True)

    class Meta:
        model = CRIMRole
        fields = (
            'url',
            'person',
            'role_type',
        )


class CRIMPieceRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimpiece-detail-data', lookup_field='piece_id')
    roles = CRIMRoleRelationshipSerializer(
        many=True,
        read_only=True,
        source='roles_as_piece',
    )
    pdf_links = serializers.SerializerMethodField()
    mei_links = serializers.SerializerMethodField()

    class Meta:
        model = CRIMPiece
        fields = (
            'url',
            'piece_id',
            'full_title',
            'roles',
            'mei_links',
            'pdf_links',
        )

    def get_pdf_links(self, obj):
        return obj.pdf_links.split('\n')

    def get_mei_links(self, obj):
        return obj.mei_links.split('\n')


class CRIMPieceRelationshipSummarySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimpiece-detail-data', lookup_field='piece_id')

    class Meta:
        model = CRIMPiece
        fields = (
            'url',
            'piece_id',
            'full_title',
        )


# Deprecated class
class CRIMObservationRelationshipListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimobservation-detail-data', lookup_field='id')
    piece = CRIMPieceRelationshipSummarySerializer(read_only=True)

    class Meta:
        model = CRIMObservation
        fields = (
            'url',
            'id',
            'piece',
            'ema',
        )

class CJObservationRelationshipListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cjobservation-detail-data', lookup_field='id')
    piece = CRIMPieceRelationshipSummarySerializer(read_only=True)

    class Meta:
        model = CJObservation
        fields = (
            'url',
            'id',
            'piece',
            'ema',
        )


# Deprecated class
class CRIMObservationRelationshipDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimobservation-detail-data', lookup_field='id')
    observer = CRIMPersonRelationshipSerializer(read_only=True)
    piece = CRIMPieceRelationshipSerializer(read_only=True)

    class Meta:
        model = CRIMObservation
        fields = (
            'url',
            'id',
            'observer',
            'piece',
            'ema',
            'musical_type',
            'mt_cf',
            'mt_cf_voices',
            'mt_cf_dur',
            'mt_cf_mel',
            'mt_sog',
            'mt_sog_voices',
            'mt_sog_dur',
            'mt_sog_mel',
            'mt_sog_ostinato',
            'mt_sog_periodic',
            'mt_csog',
            'mt_csog_voices',
            'mt_csog_dur',
            'mt_csog_mel',
            'mt_cd',
            'mt_cd_voices',
            'mt_fg',
            'mt_fg_voices',
            'mt_fg_int',
            'mt_fg_tint',
            'mt_fg_periodic',
            'mt_fg_strict',
            'mt_fg_flexed',
            'mt_fg_sequential',
            'mt_fg_inverted',
            'mt_fg_retrograde',
            'mt_pe',
            'mt_pe_voices',
            'mt_pe_int',
            'mt_pe_tint',
            'mt_pe_strict',
            'mt_pe_flexed',
            'mt_pe_flt',
            'mt_pe_sequential',
            'mt_pe_added',
            'mt_pe_invertible',
            'mt_id',
            'mt_id_voices',
            'mt_id_int',
            'mt_id_tint',
            'mt_id_strict',
            'mt_id_flexed',
            'mt_id_flt',
            'mt_id_invertible',
            'mt_nid',
            'mt_nid_voices',
            'mt_nid_int',
            'mt_nid_tint',
            'mt_nid_strict',
            'mt_nid_flexed',
            'mt_nid_flt',
            'mt_nid_sequential',
            'mt_nid_invertible',
            'mt_hr',
            'mt_hr_voices',
            'mt_hr_simple',
            'mt_hr_staggered',
            'mt_hr_sequential',
            'mt_hr_fauxbourdon',
            'mt_cad',
            'mt_cad_cantizans',
            'mt_cad_tenorizans',
            'mt_cad_type',
            'mt_cad_tone',
            'mt_cad_dtv',
            'mt_cad_dti',
            'mt_int',
            'mt_int_voices',
            'mt_int_p6',
            'mt_int_p3',
            'mt_int_c35',
            'mt_int_c83',
            'mt_int_c65',
            'mt_fp',
            'mt_fp_ir',
            'mt_fp_range',
            'mt_fp_comment',
            'remarks',
            'created',
            'updated',
        )

class CJObservationRelationshipDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cjobservation-detail-data', lookup_field='id')
    observer = CRIMPersonRelationshipSerializer(read_only=True)
    piece = CRIMPieceRelationshipSerializer(read_only=True)
    definition = CRIMDefinitionObservationRelationshipSerializer(read_only=True)
    details = serializers.JSONField()

    class Meta:
        model = CJObservation
        fields = (
            'url',
            'id',
            'observer',
            'piece',
            'ema',
            'musical_type',
            'definition',
            'details',
            'remarks',
            'created',
            'updated',
        )


# Deprecated class
class CRIMRelationshipDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimrelationship-detail-data', lookup_field='id')
    observer = CRIMPersonRelationshipSerializer(read_only=True)
    model_observation = CRIMObservationRelationshipDetailSerializer(read_only=True)
    derivative_observation = CRIMObservationRelationshipDetailSerializer(read_only=True)

    class Meta:
        model = CRIMRelationship
        fields = (
            'url',
            'id',
            'observer',
            'model_observation',
            'derivative_observation',
            'relationship_type',
            'musical_type',
            'rt_q',
            'rt_q_x',
            'rt_q_monnayage',
            'rt_tm',
            'rt_tm_snd',
            'rt_tm_minv',
            'rt_tm_retrograde',
            'rt_tm_ms',
            'rt_tm_transposed',
            'rt_tm_invertible',
            'rt_tnm',
            'rt_tnm_embellished',
            'rt_tnm_reduced',
            'rt_tnm_amplified',
            'rt_tnm_truncated',
            'rt_tnm_ncs',
            'rt_tnm_ocs',
            'rt_tnm_ocst',
            'rt_tnm_nc',
            'rt_nm',
            'rt_om',
            'remarks',
            'created',
            'updated',
            'curated',
        )

class CJRelationshipDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cjrelationship-detail-data', lookup_field='id')
    observer = CRIMPersonRelationshipSerializer(read_only=True)
    model_observation = CJObservationRelationshipDetailSerializer(read_only=True)
    derivative_observation = CJObservationRelationshipDetailSerializer(read_only=True)
    definition = CRIMDefinitionRelationshipSerializer(read_only=True)
    details = serializers.JSONField()

    class Meta:
        model = CRIMRelationship
        fields = (
            'url',
            'id',
            'observer',
            'model_observation',
            'derivative_observation',
            'relationship_type',
            'musical_type',
            'definition',
            'details',
            'remarks',
            'created',
            'updated',
            'curated',
        )


# Deprecated class
class CRIMRelationshipListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimrelationship-detail-data', lookup_field='id')
    observer = CRIMPersonRelationshipSerializer(read_only=True)
    model_observation = CRIMObservationRelationshipListSerializer(read_only=True)
    derivative_observation = CRIMObservationRelationshipListSerializer(read_only=True)

    class Meta:
        model = CRIMRelationship
        fields = (
            'url',
            'id',
            'observer',
            'model_observation',
            'derivative_observation',
            'relationship_type',
            'musical_type',
            'rt_q',
            'rt_q_x',
            'rt_q_monnayage',
            'rt_tm',
            'rt_tm_snd',
            'rt_tm_minv',
            'rt_tm_retrograde',
            'rt_tm_ms',
            'rt_tm_transposed',
            'rt_tm_invertible',
            'rt_tnm',
            'rt_tnm_embellished',
            'rt_tnm_reduced',
            'rt_tnm_amplified',
            'rt_tnm_truncated',
            'rt_tnm_ncs',
            'rt_tnm_ocs',
            'rt_tnm_ocst',
            'rt_tnm_nc',
            'rt_nm',
            'rt_om',
            'remarks',
            'created',
            'updated',
            'curated',
        )

class CJRelationshipListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cjrelationship-detail-data', lookup_field='id')
    observer = CRIMPersonRelationshipSerializer(read_only=True)
    model_observation = CJObservationRelationshipListSerializer(read_only=True)
    derivative_observation = CJObservationRelationshipListSerializer(read_only=True)
    definition = CRIMDefinitionRelationshipSerializer(read_only=True)
    details = serializers.JSONField()

    class Meta:
        model = CJRelationship
        fields = (
            'url',
            'id',
            'observer',
            'model_observation',
            'derivative_observation',
            'relationship_type',
            'musical_type',
            'definition',
            'details',
            'remarks',
            'created',
            'updated',
            'curated',
        )


# Deprecated class
class CRIMRelationshipBriefSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimobservation-detail-data', lookup_field='id')
    observer = serializers.PrimaryKeyRelatedField(many=False,read_only=True)
    model_observation = CRIMObservationBriefSerializer(read_only=True)
    derivative_observation = CRIMObservationBriefSerializer(read_only=True)

    class Meta:
        model = CRIMRelationship
        fields = (
            'url',
            'id',
            'observer',
            'relationship_type',
            'model_observation',
            'derivative_observation',
        )

class CJRelationshipBriefSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cjobservation-detail-data', lookup_field='id')
    observer = serializers.PrimaryKeyRelatedField(many=False,read_only=True)
    model_observation = CJObservationBriefSerializer(read_only=True)
    derivative_observation = CJObservationBriefSerializer(read_only=True)

    class Meta:
        model = CJRelationship
        fields = (
            'url',
            'id',
            'observer',
            'relationship_type',
            'model_observation',
            'derivative_observation',
        )
